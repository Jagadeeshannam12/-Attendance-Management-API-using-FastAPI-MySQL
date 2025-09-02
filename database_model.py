from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey

Base = declarative_base()
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    roll_no = Column(String(20), unique=True, nullable=False)

# Attendance Table
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)   # "Present" or "Absent"