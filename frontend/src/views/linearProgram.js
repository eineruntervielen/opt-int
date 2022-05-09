export const SolverType = {
    "GLOP": 1,
    "CBC": 2,
    "CLP": 3,
    "BOP": 4
}
export const VariableType = {
    "REAL": 1,
    "INTEGER": 2,
    "BOOLEAN": 3
}
export const ObjectiveType = {
    "MAX": 1,
    "MIN": 2
}

export class Objective {
    constructor(objectiveType, variableCoefficients) {
        // this.objectiveType = objectiveType;
        // this.variableCoefficients = variableCoefficients;

    }
}

export class Result {
    constructor(status, objectiveValue, variableValues){
        // this.status = status;
        // this.objectiveValue = objectiveValue;
        // this.variableValues = variableValues;
    }
}

export class DecisionVariable {
    constructor(name, variableType, lower, lowerUnbound, upper, upperUnbound) {
        // this.name = name;
        // this.variableType = variableType;
        // this.lower = lower;
        // this.lowerUnbound = lowerUnbound;
        // this.upper = upper;
        // this.upperUnbound = upperUnbound;
    }
}

export class VariableCoefficient {
    constructor(variable, coefficient, inUse) {
        // this.variable = variable;
        // this.coefficient = coefficient;
        // this.inUse = inUse;

    }
}

export class Constraint {
    constructor(name, variableCoefficient, lower, lowerUnbound, upper, upperUnbound) {
        // this.name = name;
        // this.variableCoefficient = variableCoefficient;
        // this.lower = lower;
        // this.lowerUnbound = lowerUnbound;
        // this.upper = upper;
        // this.upperUnbound = upperUnbound;
    }
}

export class LinearProgram {
    constructor(variables, constraints, objective, solver) {
        // this.variables = variables;
        // this.constraints = constraints;
        // this.objective = objective;
        // this.solver = solver;
    }
}