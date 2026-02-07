from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from database import SessionLocal, Attendance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Attendance(BaseModel):
    student_id: str
    name: str

@app.get("/")
def home():
    return {"message": "Hello Backend"}

@app.post("/mark-attendance")
def mark_attendance(data: Attendance):
    db = SessionLocal()
    record = Attendance(student_id=name)
    db.add(record)
    db.commit()
    db.close()

    return {
    "status": "attendance_marked",
    "student_id": name,
    "time": record.time
    }

