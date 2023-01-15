import logging

from typing import TypedDict

from ortools.algorithms import pywrapknapsack_solver

logger = logging.getLogger()
logger.setLevel(level=0)


class KnapsackProblem(TypedDict):
    name: str
    capacities: list[int]
    weights: list[list[int | float]]
    values: list[int | float]


def create_and_solve(knapsack_problem: KnapsackProblem):
    if not len(knapsack_problem['values']) == len(knapsack_problem['weights'][0]):
        raise ValueError('Values und Weights müssen gleich lang sein')

    name: str = knapsack_problem['name']
    values: list[int] = knapsack_problem['values']
    weights: list[list[int | float]] = knapsack_problem['weights']
    capacities: list[int | float] = knapsack_problem['capacities']

    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, name)
    logger.warning("initialize solver")
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()
    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)
