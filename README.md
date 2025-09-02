
# Attendance Management API

A simple backend system to manage students and their attendance using **FastAPI** and **MySQL**.

##  Features
- Add / update / delete students
- Mark / update / delete attendance
- Get attendance history per student
- Built with FastAPI + SQLAlchemy + MySQL

##  Project Structure
attendance_api/
│── main.py # API routes
│── database.py # DB connection
│── models.py # Tables
│── schemas.py # Pydantic validation

bash
Copy code

##  Setup
1. Clone the repo:
   ```bash
   git clone:https://github.com/Jagadeeshannam12/-Attendance-Management-API-using-FastAPI-MySQL.git
   cd attendance-api
Create database in MySQL:

sql
CREATE DATABASE attendance_db;
Run the app:

uvicorn main:app --reload
Visit Swagger UI:

http://127.0.0.1:8000/docs# -Attendance-Management-API-using-FastAPI-MySQL
