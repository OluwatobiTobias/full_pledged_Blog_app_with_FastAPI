from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    adding_one_student,
    deteing_one_student,
    retrieving_all_student,
    retrieving_one_student,
    updating_one_student
)

from server.models import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel
)

router  = APIRouter()

@router.post("/", response_description="student data added to database")
async def adding_student(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await adding_one_student(student)
    return ResponseModel(new_student, "student added successfuuly")

@router.get("/", response_description="all students data retrieved")
async def get_all_students():
    students = await retrieving_all_student()
    if students:
        return ResponseModel(students, "all student data retrieved successfully")
    return ResponseModel(students, "empty list returned")

@router.get("/{id}", response_description="student data retrieved with matching id")
async def get_one_student(id):
    student = await retrieving_one_student(id)
    if student:
        return ResponseModel(student, "student data retrieved with matching id")
    return ErrorResponseModel("An error occured", 404, "student does not exist")


@router.put("/{id}")
async def updating_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    print(req, "----------")
    updated_student = await updating_one_student(id, req)
    if updated_student:
        return ResponseModel(
            f"student with ID: {id} name update is successful",
            "student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )

@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await deteing_one_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )