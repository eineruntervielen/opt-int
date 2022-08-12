from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.apps.staff_scheduling import optimize

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
def staff_scheduling_optimize():
    status = optimize()
    return {'status': status}


# @app.get("/")
# def read_root():
#     return {
#         "x": 1,
#         "y": 0
#     }
