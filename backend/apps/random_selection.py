
'''Function takes input from list and returns as dict so far'''
def random_shift_selection(shift_requests) -> dict:
    employees = shift_requests["num_employees"]
    days = shift_requests["num_days"]
    shifts = shift_requests["num_shifts"]
    return {"employees": employees, "days": days, "shifts": shifts}

    