from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.apps.staff_scheduling import create_and_solve_model, ShiftRequest, Solution

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


@app.post("/staffscheduling/")
def staff_scheduling_optimize(shift_requests: ShiftRequest) -> Solution:
    solution: Solution = create_and_solve_model(shift_requests)
    return solution
