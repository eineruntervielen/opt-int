from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.staff_scheduling import create_and_solve_model, ShiftRequest, Solution
from apps.random_selection import random_shift_selection

origins = [
    "http://localhost",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {'hello': 1}

#posting of staffscheduling result
@app.post("/staffscheduling/")
def staff_scheduling_optimize(shift_requests: ShiftRequest) -> Solution:
    solution: Solution = create_and_solve_model(shift_requests)
    return solution


#get for random selection
@app.get("/randomselection/", tags=['randomselections'])
async def get_shiftrequest() -> dict:
    return {
        "data": shift_requests
    }

#post of random selection
#so far it takes the last added list item and hands it over to not yet written function
#and returns a dictionairy with the input data
#to check if the post function works --> it does
@app.post("/randomselection/", tags=['randomselections'])
async def post_randem_selection():
    random_result = random_shift_selection(shift_requests[-1])
    return random_result


#shift DB as test_version
shift_requests = [
    { "num_employees": 6,
    "num_days": 5,
    "num_shifts": 2
    }
]