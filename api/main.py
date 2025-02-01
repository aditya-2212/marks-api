from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)

# Load student data
def load_students():
    students = {}
    with open('students.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students[row['name'].lower()] = int(row['mark'])
    return students

students = load_students()

@app.get("/api")
async def get_marks(names: list[str] = Query(...)):
    marks = [students.get(name.lower(), 0) for name in names]
    return {"marks": marks}