from ortools.sat.python.cp_model import CpModel, CpSolver, OPTIMAL
from pydantic import BaseModel


class ShiftRequest(BaseModel):
    num_employees: int
    num_days: int
    num_shifts: int
    shifts: list


class Solution(BaseModel):
    status: str
    conflicts: int
    branches: int
    wall_time: float
    objective_value: int
    reachable: int


def create_decision_variables(model: CpModel, shifts: dict, num_employees: int, num_days: int, num_shifts: int):
    """Create shift variables

    Args:
        model:
        shifts:
        num_employees:
        num_days:
        num_shifts:
    """
    for employee in range(num_employees):
        for day in range(num_days):
            for shift in range(num_shifts):
                shifts[(employee, day, shift)] = model.NewBoolVar(name=f'shift_{employee=}_{day=}_{shift=}')


def create_constraint_one_emp_per_shift(model: CpModel, shifts: dict, num_employees: int, num_days: int,
                                        num_shifts: int):
    """Each shift is assigned to exactly one nurse in .

    Args:
        model:
        shifts:
        num_employees:
        num_days:
        num_shifts:
    """
    for day in range(num_days):
        for shift in range(num_shifts):
            model.AddExactlyOne(shifts[(n, day, shift)] for n in range(num_employees))


def create_constraint_max_one_shift_per_emp(model: CpModel, shifts: dict, num_employees: int, num_days: int,
                                            num_shifts: int):
    """Each employee works at most one shift per day.

    Args:
        model:
        shifts:
        num_employees:
        num_days:
        num_shifts:
    """
    for employee in range(num_employees):
        for day in range(num_days):
            model.AddAtMostOne(shifts[(employee, day, shift)] for shift in range(num_shifts))


def create_min_max_shifts_per_employee(model: CpModel, shifts: dict, num_employees: int, num_days: int,
                                       num_shifts: int):
    """ Try to distribute the shifts evenly, so that each nurse works
    min_shifts_per_nurse shifts. If this is not possible, because the total
    number of shifts is not divisible by the number of nurses, some nurses will
    be assigned one more shift.

    Args:
        model:
        shifts:
        num_employees:
        num_days:
        num_shifts:
    """
    min_shifts_per_nurse = (num_shifts * num_days) // num_employees

    if num_shifts * num_days % num_employees == 0:
        max_shifts_per_nurse = min_shifts_per_nurse
    else:
        max_shifts_per_nurse = min_shifts_per_nurse + 1

    for n in range(num_employees):
        num_shifts_worked = 0
        for d in range(num_days):
            for s in range(num_shifts):
                num_shifts_worked += shifts[(n, d, s)]
        model.Add(min_shifts_per_nurse <= num_shifts_worked)
        model.Add(num_shifts_worked <= max_shifts_per_nurse)


def create_and_solve_model(shift_requests) -> Solution:
    """Main entry point for the REST-API.

    Args:
        shift_requests:
    """
    num_employees = shift_requests.num_employees
    num_days = shift_requests.num_days
    num_shifts = shift_requests.num_shifts
    shifts_dv = {}
    model = CpModel()

    create_decision_variables(
        model=model,
        shifts=shifts_dv,
        num_days=num_days,
        num_shifts=num_shifts,
        num_employees=num_employees
    )
    create_constraint_one_emp_per_shift(
        model=model,
        shifts=shifts_dv,
        num_days=num_days,
        num_shifts=num_shifts,
        num_employees=num_employees
    )
    create_constraint_max_one_shift_per_emp(
        model=model,
        shifts=shifts_dv,
        num_days=num_days,
        num_shifts=num_shifts,
        num_employees=num_employees
    )
    create_min_max_shifts_per_employee(
        model=model,
        shifts=shifts_dv,
        num_days=num_days,
        num_shifts=num_shifts,
        num_employees=num_employees
    )

    model.Maximize(
        sum(
            shift_requests.shifts[n][d][s] * shifts_dv[(n, d, s)]
            for n in range(num_employees)
            for d in range(num_days)
            for s in range(num_shifts)
        )
    )

    # Creates the solver and solve.
    solver = CpSolver()
    status = solver.Solve(model)

    if status == OPTIMAL:
        min_shifts_per_nurse = (num_shifts * num_days) // num_employees
        print('Solution:')
        for d in range(num_days):
            print('Day', d)
            for n in range(num_employees):
                for s in range(num_shifts):
                    if solver.Value(shifts_dv[(n, d, s)]) == 1:
                        if shift_requests.shifts[n][d][s] == True:
                            print('Nurse', n, 'works shift', s, '(requested).')
                        else:
                            print('Nurse', n, 'works shift', s, '(not requested).')
            print()
        print(f'Number of shift requests met = {solver.ObjectiveValue()}',
              f'(out of {num_employees * min_shifts_per_nurse})')
    else:
        print('No optimal solution found !')

    # Statistics.
    print('\nStatistics')
    print('  - status: %s' % solver.StatusName())
    print('  - conflicts: %i' % solver.NumConflicts())
    print('  - branches : %i' % solver.NumBranches())
    print('  - wall time: %f s' % solver.WallTime())

    s = Solution(
        status=solver.StatusName(),
        conflicts=solver.NumConflicts(),
        branches=solver.NumBranches(),
        wall_time=solver.WallTime(),
        objective_value=solver.ObjectiveValue(),
        reachable=num_employees * min_shifts_per_nurse
    )
    return s
