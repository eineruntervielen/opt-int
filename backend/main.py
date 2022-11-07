from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.staff_scheduling import create_and_solve_model, ShiftRequest, Solution

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
@app.post("/randomselection/", tags=['randomselections'])
async def post_randem_selection() -> dict:
    employees = shift_requests[-1]["num_employees"]
    days = shift_requests[-1]["num_days"]
    shifts = shift_requests[-1]["num_shifts"]
    return "We have %s employees, who have to cover %s days with each %s shifts." %(employees,days,shifts)


#shift DB as test_version
shift_requests = [
    { "num_employees": 10,
    "num_days": 5,
    "num_shifts": 2
    }
]