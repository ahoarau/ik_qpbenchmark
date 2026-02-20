# Scenarios test set (Talos)

| Number of problems | 1 |
|:-------------------|:--------------------|
| Benchmark version  | 2.5.0 |
| Date               | 2026-02-20 14:17:37.597562+00:00 |
| CPU                | [AMD Ryzen Threadripper PRO 7955WX 16-Cores](#cpu-info) |
| Run by             | [@qpbenchmark-user](https://github.com/qpbenchmark-user/) |

Benchmark reports are copious as we aim to document comparison factors as much as possible. You can also [jump to results](#results-by-settings) directly.

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Results by settings](#results-by-settings)
    * [Default settings](#default-settings)
    * [High accuracy settings](#high-accuracy-settings)
    * [Low accuracy settings](#low-accuracy-settings)
    * [Mid accuracy settings](#mid-accuracy-settings)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)
* [Settings](#settings)
* [Known limitations](#known-limitations)
* [CPU info](#cpu-info)

## Description

Differential inverse kinematics QP problems generated from Talos robot motions (static and trajectory)

## Solvers

| solver      | version               |
|:------------|:----------------------|
| clarabel    | 0.11.1                |
| cvxopt      | 1.3.2                 |
| daqp        | 0.7.1                 |
| ecos        | 2.0.14                |
| gurobi      | 13.0.1 (size-limited) |
| highs       | 1.13.1                |
| jaxopt_osqp | 0.8.4                 |
| kvxopt      | 1.3.2.4               |
| piqp        | 0.6.2                 |
| proxqp      | 0.7.2                 |
| qpalm       | 1.2.6                 |
| quadprog    | 0.1.13                |
| scs         | 3.2.11                |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.8.2.

## Results by settings

### Default settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  4.2 |                                      3181.0 |                                     1.0 |                               527.6 |
| cvxopt      |                               100.0 |                                 12.0 |                                         1.0 |                                     1.0 |                              3800.0 |
| daqp        |                                 0.0 |                              27053.2 |                           562949953421313.0 |                       562949953421313.0 |                      860779745292.5 |
| ecos        |                               100.0 |                                  5.5 |                                       304.0 |                             114536700.0 |                              3158.2 |
| gurobi      |                               100.0 |                                 20.5 |                                         1.0 |                                    99.0 |                               164.1 |
| highs       |                               100.0 |                                  9.9 |                                         1.0 |                                394061.0 |                                50.2 |
| jaxopt_osqp |                               100.0 |                               2175.7 |                                5029272065.0 |                          332445262392.0 |                           9743185.4 |
| kvxopt      |                               100.0 |                                  9.2 |                                         1.0 |                                     1.0 |                              3800.0 |
| piqp        |                               100.0 |                                  2.7 |                                         1.0 |                                  4509.0 |                               292.0 |
| proxqp      |                               100.0 |                                  2.3 |                                 229498763.0 |                                 11749.0 |                       11901629822.1 |
| qpalm       |                               100.0 |                                  1.8 |                                7945738324.0 |                                823379.0 |                          40546375.6 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                123184.0 |                                 1.0 |
| scs         |                               100.0 |                                  2.6 |                                 326095598.0 |                             296218414.0 |                            484316.2 |

### High accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  3.0 |                                      3181.0 |                                     1.0 |                              1540.4 |
| cvxopt      |                                 0.0 |                                 13.0 |                                         1.0 |                                     1.0 |                             11094.8 |
| daqp        |                                 0.0 |                              23789.5 |                                    562951.0 |                                562951.0 |                              2513.2 |
| ecos        |                                 0.0 |                                  4.7 |                                       304.0 |                             114536700.0 |                              9220.7 |
| gurobi      |                               100.0 |                                 16.3 |                                         1.0 |                                    99.0 |                               479.0 |
| highs       |                               100.0 |                                  7.2 |                                         1.0 |                                394061.0 |                               146.6 |
| jaxopt_osqp |                                 0.0 |                              23789.5 |                                    562951.0 |                                562951.0 |                              2513.2 |
| kvxopt      |                                 0.0 |                                  7.1 |                                         1.0 |                                     1.0 |                             11094.8 |
| piqp        |                               100.0 |                                  2.6 |                                         1.0 |                                  4509.0 |                               852.5 |
| proxqp      |                                 0.0 |                              23789.5 |                                    562951.0 |                                562951.0 |                              2513.2 |
| qpalm       |                               100.0 |                                  3.0 |                                      8946.0 |                                    11.0 |                                93.1 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                123184.0 |                                 2.9 |
| scs         |                               100.0 |                                  2.5 |                                     43019.0 |                                320249.0 |                                 1.0 |

### Low accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  6.6 |                                3183503556.0 |                                     1.0 |                      345353841240.0 |
| cvxopt      |                               100.0 |                                 32.3 |                                         1.0 |                                     1.0 |                           2485231.0 |
| daqp        |                                 0.0 |                                  1.0 |                          1329739382655941.0 |                                     1.0 |                                 1.0 |
| ecos        |                               100.0 |                                 16.8 |                                       304.0 |                             114536700.0 |                           2065436.0 |
| gurobi      |                               100.0 |                                 48.9 |                                         1.0 |                                    99.0 |                            107296.0 |
| highs       |                               100.0 |                                 24.1 |                                         1.0 |                                394061.0 |                             32846.0 |
| jaxopt_osqp |                               100.0 |                               5655.4 |                                5029272065.0 |                          332445262392.0 |                        6372043282.0 |
| kvxopt      |                               100.0 |                                 29.1 |                                         1.0 |                                     1.0 |                           2485231.0 |
| piqp        |                               100.0 |                                  7.6 |                                         1.0 |                            4508910544.0 |                      190882183376.0 |
| proxqp      |                                 0.0 |                              70417.6 |                              562949953420.0 |                          562949953420.0 |                      562949953420.0 |
| qpalm       |                               100.0 |                                  2.6 |                                7945738324.0 |                                823379.0 |                       26517329615.0 |
| quadprog    |                               100.0 |                                  3.3 |                                         1.0 |                                123184.0 |                               654.0 |
| scs         |                               100.0 |                                  4.7 |                                 326095598.0 |                             296218414.0 |                         316742770.0 |

### Mid accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                  2.1 |                                    318061.0 |                                     1.0 |                             52759.2 |
| cvxopt      |                               100.0 |                                 11.3 |                                         1.0 |                                     1.0 |                              3800.0 |
| daqp        |                                 0.0 |                              24463.4 |                                 562949952.0 |                             562949952.0 |                            860779.7 |
| ecos        |                               100.0 |                                  5.1 |                                       304.0 |                             114536700.0 |                              3158.2 |
| gurobi      |                               100.0 |                                 18.7 |                                         1.0 |                                    99.0 |                               164.1 |
| highs       |                               100.0 |                                  8.6 |                                         1.0 |                                394061.0 |                                50.2 |
| jaxopt_osqp |                               100.0 |                               1964.8 |                                  12816786.0 |                             220739058.0 |                             10587.2 |
| kvxopt      |                               100.0 |                                 10.2 |                                         1.0 |                                     1.0 |                              3800.0 |
| piqp        |                               100.0 |                                  2.2 |                                         1.0 |                                450891.0 |                             29194.8 |
| proxqp      |                                 0.0 |                              24463.4 |                                 562949952.0 |                             562949952.0 |                            860779.7 |
| qpalm       |                               100.0 |                                  3.4 |                                  12029539.0 |                                  1109.0 |                             35596.5 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                123184.0 |                                 1.0 |
| scs         |                               100.0 |                                  1.9 |                                  15362114.0 |                              17148161.0 |                              1216.4 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |               0 |            100 |            100 |
| daqp        |         0 |               0 |              0 |              0 |
| ecos        |       100 |               0 |            100 |            100 |
| gurobi      |       100 |             100 |            100 |            100 |
| highs       |       100 |             100 |            100 |            100 |
| jaxopt_osqp |       100 |               0 |            100 |            100 |
| kvxopt      |       100 |               0 |            100 |            100 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |               0 |              0 |              0 |
| qpalm       |       100 |             100 |            100 |            100 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |             100 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |             100 |            100 |            100 |
| cvxopt      |       100 |               0 |            100 |            100 |
| daqp        |       100 |             100 |              0 |            100 |
| ecos        |       100 |               0 |            100 |            100 |
| gurobi      |       100 |             100 |            100 |            100 |
| highs       |       100 |             100 |            100 |            100 |
| jaxopt_osqp |       100 |             100 |            100 |            100 |
| kvxopt      |       100 |               0 |            100 |            100 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |             100 |            100 |            100 |
| qpalm       |       100 |             100 |            100 |            100 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |             100 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       4.2 |             3.0 |            6.6 |            2.1 |
| cvxopt      |      12.0 |            13.0 |           32.3 |           11.3 |
| daqp        |   27053.2 |         23789.5 |            1.0 |        24463.4 |
| ecos        |       5.5 |             4.7 |           16.8 |            5.1 |
| gurobi      |      20.5 |            16.3 |           48.9 |           18.7 |
| highs       |       9.9 |             7.2 |           24.1 |            8.6 |
| jaxopt_osqp |    2175.7 |         23789.5 |         5655.4 |         1964.8 |
| kvxopt      |       9.2 |             7.1 |           29.1 |           10.2 |
| piqp        |       2.7 |             2.6 |            7.6 |            2.2 |
| proxqp      |       2.3 |         23789.5 |        70417.6 |        24463.4 |
| qpalm       |       1.8 |             3.0 |            2.6 |            3.4 |
| quadprog    |       1.0 |             1.0 |            3.3 |            1.0 |
| scs         |       2.6 |             2.5 |            4.7 |            1.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|             |           default |   high_accuracy |       low_accuracy |   mid_accuracy |
|:------------|------------------:|----------------:|-------------------:|---------------:|
| clarabel    |            3181.0 |          3181.0 |       3183503556.0 |       318061.0 |
| cvxopt      |               1.0 |             1.0 |                1.0 |            1.0 |
| daqp        | 562949953421313.0 |        562951.0 | 1329739382655941.0 |    562949952.0 |
| ecos        |             304.0 |           304.0 |              304.0 |          304.0 |
| gurobi      |               1.0 |             1.0 |                1.0 |            1.0 |
| highs       |               1.0 |             1.0 |                1.0 |            1.0 |
| jaxopt_osqp |      5029272065.0 |        562951.0 |       5029272065.0 |     12816786.0 |
| kvxopt      |               1.0 |             1.0 |                1.0 |            1.0 |
| piqp        |               1.0 |             1.0 |                1.0 |            1.0 |
| proxqp      |       229498763.0 |        562951.0 |     562949953420.0 |    562949952.0 |
| qpalm       |      7945738324.0 |          8946.0 |       7945738324.0 |     12029539.0 |
| quadprog    |               1.0 |             1.0 |                1.0 |            1.0 |
| scs         |       326095598.0 |         43019.0 |        326095598.0 |     15362114.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|             |           default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|------------------:|----------------:|---------------:|---------------:|
| clarabel    |               1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt      |               1.0 |             1.0 |            1.0 |            1.0 |
| daqp        | 562949953421313.0 |        562951.0 |            1.0 |    562949952.0 |
| ecos        |       114536700.0 |     114536700.0 |    114536700.0 |    114536700.0 |
| gurobi      |              99.0 |            99.0 |           99.0 |           99.0 |
| highs       |          394061.0 |        394061.0 |       394061.0 |       394061.0 |
| jaxopt_osqp |    332445262392.0 |        562951.0 | 332445262392.0 |    220739058.0 |
| kvxopt      |               1.0 |             1.0 |            1.0 |            1.0 |
| piqp        |            4509.0 |          4509.0 |   4508910544.0 |       450891.0 |
| proxqp      |           11749.0 |        562951.0 | 562949953420.0 |    562949952.0 |
| qpalm       |          823379.0 |            11.0 |       823379.0 |         1109.0 |
| quadprog    |          123184.0 |        123184.0 |       123184.0 |       123184.0 |
| scs         |       296218414.0 |        320249.0 |    296218414.0 |     17148161.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|             |        default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|---------------:|----------------:|---------------:|---------------:|
| clarabel    |          527.6 |          1540.4 | 345353841240.0 |        52759.2 |
| cvxopt      |         3800.0 |         11094.8 |      2485231.0 |         3800.0 |
| daqp        | 860779745292.5 |          2513.2 |            1.0 |       860779.7 |
| ecos        |         3158.2 |          9220.7 |      2065436.0 |         3158.2 |
| gurobi      |          164.1 |           479.0 |       107296.0 |          164.1 |
| highs       |           50.2 |           146.6 |        32846.0 |           50.2 |
| jaxopt_osqp |      9743185.4 |          2513.2 |   6372043282.0 |        10587.2 |
| kvxopt      |         3800.0 |         11094.8 |      2485231.0 |         3800.0 |
| piqp        |          292.0 |           852.5 | 190882183376.0 |        29194.8 |
| proxqp      |  11901629822.1 |          2513.2 | 562949953420.0 |       860779.7 |
| qpalm       |     40546375.6 |            93.1 |  26517329615.0 |        35596.5 |
| quadprog    |            1.0 |             2.9 |          654.0 |            1.0 |
| scs         |       484316.2 |             1.0 |    316742770.0 |         1216.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).

## Settings

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |        10 |          10     |         10     |         10     |

Solvers for each settings are configured as follows:

| solver      | parameter                        | default   |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|:---------------------------------|:----------|----------------:|---------------:|---------------:|
| clarabel    | ``max_threads``                  | 1         |           1     |          1     |          1     |
| clarabel    | ``tol_feas``                     | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel    | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel    | ``tol_gap_rel``                  | -         |           0     |          0     |          0     |
| cvxopt      | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| daqp        | ``dual_tol``                     | -         |           1e-09 |          0.001 |          1e-06 |
| daqp        | ``primal_tol``                   | -         |           1e-09 |          0.001 |          1e-06 |
| ecos        | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi      | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi      | ``OptimalityTol``                | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi      | ``Threads``                      | 1         |           1     |          1     |          1     |
| gurobi      | ``TimeLimit``                    | 10.0      |          10     |         10     |         10     |
| highs       | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |          1e-06 |
| highs       | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |          1e-06 |
| highs       | ``threads``                      | 1         |           1     |          1     |          1     |
| highs       | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| jaxopt_osqp | ``tol``                          | -         |           1e-09 |          0.001 |          1e-06 |
| kvxopt      | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| piqp        | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| piqp        | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| piqp        | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| piqp        | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| piqp        | ``eps_rel``                      | -         |           0     |          0     |          0     |
| proxqp      | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| proxqp      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp      | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp      | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| proxqp      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm       | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| qpalm       | ``eps_rel``                      | -         |           0     |          0     |          0     |
| qpalm       | ``time_limit``                   | 10.0      |          10     |         10     |         10     |
| scs         | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| scs         | ``eps_rel``                      | -         |           0     |          0     |          0     |
| scs         | ``time_limit_secs``              | 10.0      |          10     |         10     |         10     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS
- [#88](https://github.com/qpsolvers/qpbenchmark/issues/88): CPU thermal throttling

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | AMD Ryzen Threadripper PRO 7955WX 16-Cores |
| `count` | 32 |
| `family` | 25 |
| `flags` | `3dnow`, `3dnowprefetch`, `abm`, `adx`, `aes`, `apic`, `arat`, `avx`, `avx2`, `avx512_bf16`, `avx512_bitalg`, `avx512_vbmi2`, `avx512_vnni`, `avx512_vpopcntdq`, `avx512bitalg`, `avx512bw`, `avx512cd`, `avx512dq`, `avx512f`, `avx512ifma`, `avx512vbmi`, `avx512vbmi2`, `avx512vl`, `avx512vnni`, `avx512vpopcntdq`, `bmi1`, `bmi2`, `clflush`, `clflushopt`, `clwb`, `clzero`, `cmov`, `cmp_legacy`, `constant_tsc`, `cpuid`, `cr8_legacy`, `cx16`, `cx8`, `de`, `decodeassists`, `erms`, `extd_apicid`, `f16c`, `flushbyasid`, `fma`, `fpu`, `fsgsbase`, `fsrm`, `fxsr`, `fxsr_opt`, `gfni`, `ht`, `hypervisor`, `ibpb`, `ibrs`, `invpcid`, `lahf_lm`, `lm`, `mca`, `mce`, `misalignsse`, `mmx`, `mmxext`, `movbe`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `npt`, `nrip_save`, `nx`, `osvw`, `osxsave`, `pae`, `pat`, `pausefilter`, `pcid`, `pclmulqdq`, `pdpe1gb`, `perfctr_core`, `pfthreshold`, `pge`, `pni`, `popcnt`, `pse`, `pse36`, `rdpid`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sep`, `sha`, `sha_ni`, `smap`, `smep`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `sse4a`, `ssse3`, `stibp`, `svm`, `syscall`, `topoext`, `tsc`, `tsc_known_freq`, `tsc_reliable`, `tsc_scale`, `umip`, `v_vmsave_vmload`, `vaes`, `vmcb_clean`, `vme`, `vmmcall`, `vpclmulqdq`, `xgetbv1`, `xsave`, `xsavec`, `xsaveerptr`, `xsaveopt`, `xsaves` |
| `l1_data_cache_size` | 524288 |
| `l1_instruction_cache_size` | 524288 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 1024 |
| `l2_cache_size` | 16777216 |
| `l3_cache_size` | 1048576 |
| `model` | 24 |
| `python_version` | 3.12.12.final.0 (64 bit) |
| `stepping` | 1 |
| `vendor_id_raw` | AuthenticAMD |

