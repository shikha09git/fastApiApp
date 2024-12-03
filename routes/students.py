from fastapi import APIRouter, HTTPException
from database import students_collection
from models import Student
from bson import ObjectId

router = APIRouter()

@router.post("/students", status_code=201)
async def create_student(student: Student):
    student_dict = student.dict(exclude={"id"})
    result = await students_collection.insert_one(student_dict)
    student.id = str(result.inserted_id)
    return student

@router.get("/students")
async def get_students():
    students = await students_collection.find().to_list(100)
    for student in students:
        student["id"] = str(student["_id"])
        del student["_id"]
    return students

@router.get("/students/{id}")
async def get_student(id: str):
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student["id"] = str(student["_id"])
    del student["_id"]
    return student

@router.put("/students/{id}")
async def update_student(id: str, updated_data: Student):
    update = updated_data.dict(exclude={"id"})
    result = await students_collection.update_one({"_id": ObjectId(id)}, {"$set": update})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return await get_student(id)

@router.delete("/students/{id}", status_code=204)
async def delete_student(id: str):
    result = await students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return None
