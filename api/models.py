from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Machine(Base):
    __tablename__ = "machines"

    machineName = Column(String, primary_key=True, index=True)
    machineType = Column(String, index=True)
    machineLocation = Column(String)
    machineStatus = Column(String)

    # job_list = relationship("Job", back_populates="status")

class Job(Base):
    __tablename__ = "jobs"
    job_id = Column(Integer, primary_key = True, index = True)
    # machineName = Column(String, ForeignKey("machines.name"))
    due = Column(String)
    part_no = Column(String)
    customer = Column(String)

    # status = relationship("Machine", back_populates="job_list")

print("models complete")