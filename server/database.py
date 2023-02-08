from motor import motor_asyncio
from .models import StudentSchema
from typing import Dict

MONGO_DB = "mongodb://localhost:27017"
client = motor_asyncio.AsyncIOMotorClient(MONGO_DB)
database = client.students
student_collection = database.get_collection('student_collection')

def helper_func(student: StudentSchema) -> Dict:
    ...


