from motor import motor_asyncio
from .models import StudentSchema
from typing import Dict, List
from bson.objectid import ObjectId

MONGO_DB = "mongodb://localhost:27017"
client = motor_asyncio.AsyncIOMotorClient(MONGO_DB)
database = client.students
student_collection = database.get_collection('student_collection')

def helper_func(student) -> Dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["full_name"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }

async def retrieving_all_student():
    students_list: List = []
    async for student in student_collection.find():
        students_list.append(helper_func(student))
    return students_list


async def adding_one_student(student_data: Dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return helper_func(new_student)


async def retrieving_one_student(id: str) -> Dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student: return helper_func(student)


async def updating_one_student(id: str, data: Dict) -> bool:
    if len(data) < 1:
        return False
    student =  await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
                {"_id": ObjectId(id)},{"$set": data}
                )
    if updated_student:
        print(updated_student)
        return True

    return False


async def deteing_one_student(id: str) -> bool:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True


