# IK test set (Talos)

| Number of problems | 1 |
|:-------------------|:--------------------|
| Benchmark version  | 2.5.0 |
| Date               | 2026-02-20 14:17:53.614604+00:00 |
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

Differential inverse kinematics QP problems generated from Pink scenarios (Talos robot)

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
| clarabel    |                               100.0 |                                  7.6 |                                         1.0 |                               2967116.0 |                             38156.0 |
| cvxopt      |                               100.0 |                                 19.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp        |                               100.0 |                                  1.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos        |                               100.0 |                                  4.6 |                                         1.0 |                           17844077727.0 |                         396811733.0 |
| gurobi      |                               100.0 |                                390.2 |                                         1.0 |                                    11.0 |                                 1.0 |
| highs       |                               100.0 |                                  7.9 |                                         1.0 |                               7874891.0 |                           1683671.0 |
| jaxopt_osqp |                               100.0 |                                 33.9 |                                         1.0 |                               2156289.0 |                             27726.0 |
| kvxopt      |                               100.0 |                                 51.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp        |                               100.0 |                                  6.9 |                                         1.0 |                              26655206.0 |                            590646.0 |
| piqp        |                               100.0 |                                  1.9 |                                         1.0 |                                 97199.0 |                             20954.0 |
| proxqp      |                               100.0 |                                  4.3 |                                         1.0 |                              84757642.0 |                          18431939.0 |
| qpalm       |                               100.0 |                                  4.0 |                                         1.0 |                                    79.0 |                                16.0 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs         |                               100.0 |                                 10.5 |                                         1.0 |                               2967116.0 |                             38156.0 |

### High accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                                 0.0 |                                  9.1 |                                         1.0 |                               2967116.0 |                             38156.0 |
| cvxopt      |                               100.0 |                                  2.6 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp        |                               100.0 |                                  1.3 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos        |                                 0.0 |                                  4.6 |                                         1.0 |                           17844077727.0 |                         396811733.0 |
| gurobi      |                               100.0 |                                 25.5 |                                         1.0 |                                    11.0 |                                 1.0 |
| highs       |                                 0.0 |                                  3.2 |                                         1.0 |                               7874891.0 |                           1683671.0 |
| jaxopt_osqp |                                 0.0 |                                  5.3 |                                         1.0 |                               2156289.0 |                             27726.0 |
| kvxopt      |                               100.0 |                                  3.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp        |                               100.0 |                                  7.1 |                                         1.0 |                                    76.0 |                                 1.0 |
| piqp        |                               100.0 |                                  1.3 |                                         1.0 |                                 97199.0 |                             20954.0 |
| proxqp      |                               100.0 |                                  1.2 |                                         1.0 |                                 97199.0 |                             20954.0 |
| qpalm       |                               100.0 |                                  3.0 |                                         1.0 |                                    79.0 |                                16.0 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs         |                                 0.0 |                                 10.3 |                                         1.0 |                               2967116.0 |                             38156.0 |

### Low accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                 11.2 |                                         1.0 |                               2967116.0 |                             38156.0 |
| cvxopt      |                               100.0 |                                  2.9 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp        |                               100.0 |                                  1.2 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos        |                               100.0 |                                  5.5 |                                         1.0 |                           17844077727.0 |                         396811733.0 |
| gurobi      |                               100.0 |                                 29.9 |                                         1.0 |                                    11.0 |                                 1.0 |
| highs       |                               100.0 |                                  3.4 |                                         1.0 |                               7874891.0 |                           1683671.0 |
| jaxopt_osqp |                               100.0 |                                  5.0 |                                         1.0 |                               2156289.0 |                             27726.0 |
| kvxopt      |                               100.0 |                                  3.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp        |                               100.0 |                                  8.0 |                                         1.0 |                              26655206.0 |                            590646.0 |
| piqp        |                               100.0 |                                  1.2 |                                         1.0 |                              84757642.0 |                          18431939.0 |
| proxqp      |                               100.0 |                                  1.0 |                                         1.0 |                              84757642.0 |                          18431939.0 |
| qpalm       |                               100.0 |                                  3.3 |                                         1.0 |                                    79.0 |                                16.0 |
| quadprog    |                               100.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs         |                               100.0 |                                 11.2 |                                         1.0 |                               2967116.0 |                             38156.0 |

### Mid accuracy settings

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|             |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |
|:------------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|
| clarabel    |                               100.0 |                                 11.1 |                                         1.0 |                               2967116.0 |                             38156.0 |
| cvxopt      |                               100.0 |                                  2.8 |                                         1.0 |                                     1.0 |                                 1.0 |
| daqp        |                               100.0 |                                  1.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| ecos        |                                 0.0 |                                  5.4 |                                         1.0 |                           17844077727.0 |                         396811733.0 |
| gurobi      |                               100.0 |                                 29.5 |                                         1.0 |                                    11.0 |                                 1.0 |
| highs       |                               100.0 |                                  3.4 |                                         1.0 |                               7874891.0 |                           1683671.0 |
| jaxopt_osqp |                               100.0 |                                  4.8 |                                         1.0 |                               2156289.0 |                             27726.0 |
| kvxopt      |                               100.0 |                                  3.4 |                                         1.0 |                                     1.0 |                                 1.0 |
| osqp        |                               100.0 |                                  8.0 |                                         1.0 |                              26655206.0 |                            590646.0 |
| piqp        |                               100.0 |                                  1.2 |                                         1.0 |                              84757642.0 |                          18431939.0 |
| proxqp      |                               100.0 |                                  1.0 |                                         1.0 |                              84757642.0 |                          18431939.0 |
| qpalm       |                               100.0 |                                  4.7 |                                         1.0 |                                    79.0 |                                16.0 |
| quadprog    |                               100.0 |                                  1.1 |                                         1.0 |                                     1.0 |                                 1.0 |
| scs         |                               100.0 |                                 11.1 |                                         1.0 |                               2967116.0 |                             38156.0 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |               0 |            100 |            100 |
| cvxopt      |       100 |             100 |            100 |            100 |
| daqp        |       100 |             100 |            100 |            100 |
| ecos        |       100 |               0 |            100 |              0 |
| gurobi      |       100 |             100 |            100 |            100 |
| highs       |       100 |               0 |            100 |            100 |
| jaxopt_osqp |       100 |               0 |            100 |            100 |
| kvxopt      |       100 |             100 |            100 |            100 |
| osqp        |       100 |             100 |            100 |            100 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |             100 |            100 |            100 |
| qpalm       |       100 |             100 |            100 |            100 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |               0 |            100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       100 |               0 |            100 |            100 |
| cvxopt      |       100 |             100 |            100 |            100 |
| daqp        |       100 |             100 |            100 |            100 |
| ecos        |       100 |               0 |            100 |              0 |
| gurobi      |       100 |             100 |            100 |            100 |
| highs       |       100 |               0 |            100 |            100 |
| jaxopt_osqp |       100 |               0 |            100 |            100 |
| kvxopt      |       100 |             100 |            100 |            100 |
| osqp        |       100 |             100 |            100 |            100 |
| piqp        |       100 |             100 |            100 |            100 |
| proxqp      |       100 |             100 |            100 |            100 |
| qpalm       |       100 |             100 |            100 |            100 |
| quadprog    |       100 |             100 |            100 |            100 |
| scs         |       100 |               0 |            100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       7.6 |             9.1 |           11.2 |           11.1 |
| cvxopt      |      19.8 |             2.6 |            2.9 |            2.8 |
| daqp        |       1.1 |             1.3 |            1.2 |            1.1 |
| ecos        |       4.6 |             4.6 |            5.5 |            5.4 |
| gurobi      |     390.2 |            25.5 |           29.9 |           29.5 |
| highs       |       7.9 |             3.2 |            3.4 |            3.4 |
| jaxopt_osqp |      33.9 |             5.3 |            5.0 |            4.8 |
| kvxopt      |      51.8 |             3.8 |            3.8 |            3.4 |
| osqp        |       6.9 |             7.1 |            8.0 |            8.0 |
| piqp        |       1.9 |             1.3 |            1.2 |            1.2 |
| proxqp      |       4.3 |             1.2 |            1.0 |            1.0 |
| qpalm       |       4.0 |             3.0 |            3.3 |            4.7 |
| quadprog    |       1.0 |             1.0 |            1.0 |            1.1 |
| scs         |      10.5 |            10.3 |           11.2 |           11.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|             |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| clarabel    |       1.0 |             1.0 |            1.0 |            1.0 |
| cvxopt      |       1.0 |             1.0 |            1.0 |            1.0 |
| daqp        |       1.0 |             1.0 |            1.0 |            1.0 |
| ecos        |       1.0 |             1.0 |            1.0 |            1.0 |
| gurobi      |       1.0 |             1.0 |            1.0 |            1.0 |
| highs       |       1.0 |             1.0 |            1.0 |            1.0 |
| jaxopt_osqp |       1.0 |             1.0 |            1.0 |            1.0 |
| kvxopt      |       1.0 |             1.0 |            1.0 |            1.0 |
| osqp        |       1.0 |             1.0 |            1.0 |            1.0 |
| piqp        |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp      |       1.0 |             1.0 |            1.0 |            1.0 |
| qpalm       |       1.0 |             1.0 |            1.0 |            1.0 |
| quadprog    |       1.0 |             1.0 |            1.0 |            1.0 |
| scs         |       1.0 |             1.0 |            1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|             |       default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|--------------:|----------------:|---------------:|---------------:|
| clarabel    |     2967116.0 |       2967116.0 |      2967116.0 |      2967116.0 |
| cvxopt      |           1.0 |             1.0 |            1.0 |            1.0 |
| daqp        |           1.0 |             1.0 |            1.0 |            1.0 |
| ecos        | 17844077727.0 |   17844077727.0 |  17844077727.0 |  17844077727.0 |
| gurobi      |          11.0 |            11.0 |           11.0 |           11.0 |
| highs       |     7874891.0 |       7874891.0 |      7874891.0 |      7874891.0 |
| jaxopt_osqp |     2156289.0 |       2156289.0 |      2156289.0 |      2156289.0 |
| kvxopt      |           1.0 |             1.0 |            1.0 |            1.0 |
| osqp        |    26655206.0 |            76.0 |     26655206.0 |     26655206.0 |
| piqp        |       97199.0 |         97199.0 |     84757642.0 |     84757642.0 |
| proxqp      |    84757642.0 |         97199.0 |     84757642.0 |     84757642.0 |
| qpalm       |          79.0 |            79.0 |           79.0 |           79.0 |
| quadprog    |           1.0 |             1.0 |            1.0 |            1.0 |
| scs         |     2967116.0 |       2967116.0 |      2967116.0 |      2967116.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|             |     default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|------------:|----------------:|---------------:|---------------:|
| clarabel    |     38156.0 |         38156.0 |        38156.0 |        38156.0 |
| cvxopt      |         1.0 |             1.0 |            1.0 |            1.0 |
| daqp        |         1.0 |             1.0 |            1.0 |            1.0 |
| ecos        | 396811733.0 |     396811733.0 |    396811733.0 |    396811733.0 |
| gurobi      |         1.0 |             1.0 |            1.0 |            1.0 |
| highs       |   1683671.0 |       1683671.0 |      1683671.0 |      1683671.0 |
| jaxopt_osqp |     27726.0 |         27726.0 |        27726.0 |        27726.0 |
| kvxopt      |         1.0 |             1.0 |            1.0 |            1.0 |
| osqp        |    590646.0 |             1.0 |       590646.0 |       590646.0 |
| piqp        |     20954.0 |         20954.0 |     18431939.0 |     18431939.0 |
| proxqp      |  18431939.0 |         20954.0 |     18431939.0 |     18431939.0 |
| qpalm       |        16.0 |            16.0 |           16.0 |           16.0 |
| quadprog    |         1.0 |             1.0 |            1.0 |            1.0 |
| scs         |     38156.0 |         38156.0 |        38156.0 |        38156.0 |

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

