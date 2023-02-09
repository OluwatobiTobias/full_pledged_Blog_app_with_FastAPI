from motor import motor_asyncio
from typing import Dict, List
from bson.objectid import ObjectId

MONGO_DB = "mongodb://localhost:27017"
client = motor_asyncio.AsyncIOMotorClient(MONGO_DB)
database = client.users
user_collection = database.get_collection('user_collection')

def helper_func(user) -> Dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["full_name"],
        "email": user["email"],
        "course_of_study": user["course_of_study"],
        "year": user["year"],
        "GPA": user["gpa"],
    }

async def retrieving_all_users():
    user_list: List = []
    async for user in user_collection.find():
        user_list.append(helper_func(user))
    return user_list


async def adding_one_user(user_data: Dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return helper_func(new_user)


async def retrieving_one_user(id: str) -> Dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user: return helper_func(user)


async def updating_one_user(id: str, data: Dict) -> bool:
    if len(data) < 1:
        return False
    user =  await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
                {"_id": ObjectId(id)},{"$set": data}
                )
    if updated_user:
        return True

    return False


async def deleting_one_user(id: str) -> bool:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True


