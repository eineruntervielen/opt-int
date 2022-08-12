import datetime as dt
from pydantic import BaseModel


class Solution(BaseModel):
    conflicts: int
    branches: int
    wall_time: dt.timedelta


class Employee(BaseModel):
    id: int
    last_name: str
    first_name: str
