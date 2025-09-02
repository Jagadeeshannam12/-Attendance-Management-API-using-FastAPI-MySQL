from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import  engine, Session
import model, database_model

# Create tables in MySQL (if not exist)
database_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# ------------------ Routes ------------------

# Add a student
@app.post("/students/", response_model=model.Student)
def add_student(student: model.StudentCreate, db: Session = Depends(get_db)):
    new_student = database_model.Student(name=student.name, roll_no=student.roll_no)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Get all students
@app.get("/students/", response_model=list[model.Student])
def get_students(db: Session = Depends(get_db)):
    return db.query(database_model.Student).all()

# Mark attendance
@app.post("/attendance/", response_model=model.Attendance)
def mark_attendance(att: model.AttendanceCreate, db: Session = Depends(get_db)):
    new_att = database_model.Attendance(student_id=att.student_id, date=att.date, status=att.status)
    db.add(new_att)
    db.commit()
    db.refresh(new_att)
    return new_att

# Get attendance for a student
@app.get("/attendance/{student_id}", response_model=list[model.Attendance])
def get_attendance(student_id: int, db: Session = Depends(get_db)):
    return db.query(database_model.Attendance).filter(database_model.Attendance.student_id == student_id).all()

@app.put("/student/{student_id}")
def update_student(student_id:int,student:model.StudentCreate,db:Session=Depends(get_db)):
    stud=db.query(database_model.Student).filter(database_model.Student.id==student_id).first()
    if not stud:
        return {"Error":"Student not found"}
    stud.name=student.name
    stud.roll_no=student.roll_no
    db.commit()
    db.refresh(stud)
    return {"Success":"Student updated successfully"}
@app.delete("/stuent/{student_id}")
def delete_student(student_id:int,db:Session=Depends(get_db)):
    db.query(database_model.Attendance).filter(database_model.Attendance.student_id == student_id).delete()
    stud=db.query(database_model.Student).filter(database_model.Student.id==student_id).first()
    if not stud:
        return {"Error":"Student not found"}
    db.delete(stud)
    db.commit()
    return {"Success":"Student deleted successfully"}
@app.put("/attendance/{attendance_id}")
def update_attendance(attendance_id:int,att:model.AttendanceCreate,db:Session=Depends(get_db)):
    att_record=db.query(database_model.Attendance).filter(database_model.Attendance.id==attendance_id).first()
    if not att_record:
        return {"Error":"Attendance record not found"}
    att_record.student_id=att.student_id
    att_record.date=att.date
    att_record.status=att.status
    db.commit()
    db.refresh(att_record)
    return {"Success":"Attendance record updated successfully"}
@app.delete("/attendance/{attendance_id}")
def delete_attendance(attendance_id:int,db:Session=Depends(get_db)):
    att_record=db.query(database_model.Attendance).filter(database_model.Attendance.id==attendance_id).first()
    if not att_record:
        return {"Error":"Attendance record not found"}
    db.delete(att_record)
    db.commit()
    return {"Success":"Attendance record deleted successfully"}
