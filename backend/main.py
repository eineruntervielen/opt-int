from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.apps.staff_scheduling import create_and_solve_model

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


@app.get("/staff_scheduling")
def staff_scheduling_optimize():
    # deserialize model coming from frontend to datatype here
    status = create_and_solve_model()
    return {'status': status}


# @app.get("/")
# def read_root():
#     return {
#         "x": 1,
#         "y": 0
#     }
