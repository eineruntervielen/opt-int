from dataclasses import dataclass
from typing import List
from enum import IntEnum

from numpy import inner


class SolverType(IntEnum):
    GLOB: 1
    CBC: 2
    CLP: 3
    BOP: 4


class VariableType(IntEnum):
    REAL: 1
    INTEGER: 2
    BOOLEAN: 3


class ObjectiveType(IntEnum):
    MAX: 1
    MIN: 2


@dataclass
class Objective:
    ...


@dataclass
class Result:
    ...


@dataclass
class DecisionVariable:
    ...


@dataclass
class VariableCoefficient:
    ...


@dataclass
class Constraint:
    ...


@dataclass
class LinearProgram:
    variables: List[DecisionVariable]
    constraints: List[Constraint]
    objective: Objective
    # solver
