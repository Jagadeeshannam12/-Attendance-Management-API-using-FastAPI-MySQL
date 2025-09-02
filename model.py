from pydantic import BaseModel
from datetime import date
class StudentBase(BaseModel):
    name: str
    roll_no: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True


# Attendance schema
class AttendanceBase(BaseModel):
    student_id: int
    date: date
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int
    class Config:
        orm_mode = True