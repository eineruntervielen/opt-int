import random 

'''Function takes input from list and returns as list so far;
Randomly distributed employees on each day & shift'''
def random_shift_selection(shift_requests):
    employees = shift_requests["num_employees"]
    days = shift_requests["num_days"]
    shifts = shift_requests["num_shifts"]
    random_shift_schedule= []


    for n in range(days):
        random_shift = []
        for i in range(shifts):
            random_shift.append(random.randint(0, (employees)-1))
        random_shift_schedule.append(random_shift)
    print(random_shift_schedule)
    return random_shift_schedule

