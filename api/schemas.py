from typing import Union
from pydantic import BaseModel

class MachineBase(BaseModel):
    machineName: str
    machineType: Union[str, None] = None
    class Config:
        orm_mode = True

class MachineCreate(MachineBase):
    pass

class Machines(MachineBase):
    machineName: int
    machineStatus: int

class Jobs(BaseModel):
    job_id: int
    due: str
    part_no: str
    customer: str

# class JobCreate(JobBase):
#     customer: str

# class Jobs(JobBase):
#     job_id: int
#     due: bool
#     # machines: list[Machines] = []
#     class Config:
#         orm_mode = True