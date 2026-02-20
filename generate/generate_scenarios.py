#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import sys
import os
import pinocchio as pin
import pink
import qpbenchmark
import numpy as np
import qpsolvers
from pink import build_ik
from pathlib import Path

def get_robot_model():
    # Try to find URDF
    try:
        import example_robot_data as erd
        robot = erd.load("ur5")
        return robot.model, robot.data
    except ImportError:
        pass
    
    # Manual fallback
    prefix = Path(sys.prefix)
    # Search for Talos first
    robot_name = "talos"
    urdf_subpath = "talos_data/robots/talos_reduced.urdf"
    
    # Check system prefix
    search_paths = [
        prefix / "share" / "example-robot-data" / "robots",
        Path(__file__).resolve().parent.parent / ".pixi" / "envs" / "default" / "share" / "example-robot-data" / "robots"
    ]
    
    urdf_path = None
    package_dirs = []
    
    for path in search_paths:
        potential_urdf = path / urdf_subpath
        if potential_urdf.exists():
            urdf_path = potential_urdf
            package_dirs = [str(path)]
            break
            
    if urdf_path is None:
        # Fallback to UR5 if Talos not found (should not happen if env is correct)
        print("Talos not found, falling back to UR5...")
        robot_name = "ur5"
        urdf_subpath = "ur_description/urdf/ur5_robot.urdf"
        for path in search_paths:
            potential_urdf = path / urdf_subpath
            if potential_urdf.exists():
                urdf_path = potential_urdf
                package_dirs = [str(path)]
                break

    if urdf_path is None or not urdf_path.exists():
        raise FileNotFoundError(f"Robot URDF not found in {search_paths}")
        
    print(f"Loading robot: {robot_name} from {urdf_path}")
    model = pin.buildModelFromUrdf(str(urdf_path))
    data = model.createData()
    return model, data

def generate_static_problems(model, data):
    problems = qpbenchmark.ProblemList()
    frame_names = [f.name for f in model.frames]
    
    # Determine EE frame based on robot
    if "arm_right_7_link" in frame_names:
        ee_name = "arm_right_7_link"
    elif "ee_link" in frame_names:
        ee_name = "ee_link"
    else:
        ee_name = frame_names[-1]
    
    print(f"Generating static IK problems for {model.name}, EE frame: {ee_name}")
    
    dt = 1e-3

    # 1. Random Seed
    for i in range(10):
        q_target = pin.randomConfiguration(model)
        pin.framesForwardKinematics(model, data, q_target)
        ee_id = model.getFrameId(ee_name)
        T_target = data.oMf[ee_id].copy()
        
        q_init = pin.randomConfiguration(model)
        configuration = pink.Configuration(model, data, q_init)
        task = pink.tasks.FrameTask(ee_name, position_cost=1.0, orientation_cost=1.0)
        task.set_target(T_target)
        
        qp = build_ik(configuration, [task], dt)
        problems.append(qpbenchmark.Problem.from_qpsolvers(qp, name=f"random_seed_{i:02d}"))

    # 2. Close Seed
    for i in range(10):
        q_target = pin.randomConfiguration(model)
        pin.framesForwardKinematics(model, data, q_target)
        ee_id = model.getFrameId(ee_name)
        T_target = data.oMf[ee_id].copy()
        
        dq = np.random.uniform(-0.1, 0.1, model.nv)
        q_init = pin.integrate(model, q_target, dq)
        
        configuration = pink.Configuration(model, data, q_init)
        task = pink.tasks.FrameTask(ee_name, position_cost=1.0, orientation_cost=1.0)
        task.set_target(T_target)
        
        qp = build_ik(configuration, [task], dt)
        problems.append(qpbenchmark.Problem.from_qpsolvers(qp, name=f"close_seed_{i:02d}"))

    # 3. Desired Seed
    for i in range(10):
        q_target = pin.randomConfiguration(model)
        pin.framesForwardKinematics(model, data, q_target)
        ee_id = model.getFrameId(ee_name)
        T_target = data.oMf[ee_id].copy()
        
        q_init = q_target
        configuration = pink.Configuration(model, data, q_init)
        task = pink.tasks.FrameTask(ee_name, position_cost=1.0, orientation_cost=1.0)
        task.set_target(T_target)
        
        qp = build_ik(configuration, [task], dt)
        problems.append(qpbenchmark.Problem.from_qpsolvers(qp, name=f"desired_seed_{i:02d}"))
        
    return problems

def generate_trajectory_problems(model, data):
    problems = qpbenchmark.ProblemList()
    frame_names = [f.name for f in model.frames]
    
    # Determine EE frame based on robot
    if "arm_right_7_link" in frame_names:
        ee_name = "arm_right_7_link"
    elif "ee_link" in frame_names:
        ee_name = "ee_link"
    else:
        ee_name = frame_names[-1]
    
    ee_id = model.getFrameId(ee_name)
    
    solver = "proxqp"
    if solver not in qpsolvers.available_solvers:
        solver = "osqp"
    if solver not in qpsolvers.available_solvers:
        print("No suitable QP solver found for simulation. Skipping trajectories.")
        return problems
        
    dt = 0.01
    print(f"Generating trajectory problems using solver {solver}...")
    
    # 4. Joint Space Trajectory
    q_init = pin.neutral(model)
    q_final = pin.randomConfiguration(model)
    duration = 3.0
    steps = int(duration / dt)
    
    configuration = pink.Configuration(model, data, q_init)
    task = pink.tasks.PostureTask(cost=1.0)
    task.set_target(q_final)
    
    for t in range(steps):
        qp = build_ik(configuration, [task], dt)
        problems.append(qpbenchmark.Problem.from_qpsolvers(qp, name=f"joint_traj_{t:04d}"))
        
        sol = qpsolvers.solve_problem(qp, solver=solver)
        if sol.x is None:
            break
        configuration.integrate_inplace(sol.x, dt)

    # 5. Cartesian Trajectory
    q_init = pin.neutral(model)
    configuration = pink.Configuration(model, data, q_init)
    pin.framesForwardKinematics(model, data, q_init)
    
    T_start = data.oMf[ee_id].copy()
    T_final = T_start.copy()
    T_final.translation[2] += 0.2 # Move up 20cm
    
    task = pink.tasks.FrameTask(ee_name, position_cost=1.0, orientation_cost=1.0)
    
    for t in range(steps):
        alpha = (t + 1) / steps
        T_cur = T_start.copy()
        T_cur.translation = (1 - alpha) * T_start.translation + alpha * T_final.translation
        task.set_target(T_cur)
        
        qp = build_ik(configuration, [task], dt)
        problems.append(qpbenchmark.Problem.from_qpsolvers(qp, name=f"cartesian_traj_{t:04d}"))
        
        sol = qpsolvers.solve_problem(qp, solver=solver)
        if sol.x is None:
            break
        configuration.integrate_inplace(sol.x, dt)
        
    return problems

def generate_all_problems():
    model, data = get_robot_model()
    problems = generate_static_problems(model, data)
    traj_problems = generate_trajectory_problems(model, data)
    problems.extend(traj_problems)
    return problems

if __name__ == "__main__":
    problems = generate_all_problems()
    output_path = Path(__file__).resolve().parent.parent / "data" / "scenarios_ik.parquet"
    problems.to_parquet(output_path)
    print(f"Saved problems to {output_path}")
