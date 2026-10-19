from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id:int
    name:str
    level:int

students=[
    Student(id=1,name='Ahmed Diab',level=3),
    Student(id=2,name='Mohamed Wael',level=3)
]

#Read and Return the Students
@app.get('/students/')
def read():
    return students

#Create and Add the new student
@app.post('/students/')
def create(New_student:Student):
    students.append(New_student)
    return students

#Update and Edit the studetn data by id
@app.put('/students/{studetn_id}')
def update(student_id:int,updated_student:Student):
    for idx,student in enumerate(students):
        if student.id==student_id:
            students[idx]=updated_student
            return updated_student
    return{"error":"Students not found"}



@app.delete('/studetns/{student_id}')
def delete(student_id:int):
    for idx,student in enumerate(students):
        if student.id==student_id:
            del students[idx]
            return{'message':'Student deleted'}
    return{'error':'Student not found'}        
        