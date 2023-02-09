from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    adding_one_user,
    deleting_one_user,
    retrieving_all_users,
    retrieving_one_user,
    updating_one_user
)

from server.models import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel
)

router  = APIRouter()

@router.post("/", response_description="user data added to database")
async def adding_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await adding_one_user(user)
    return ResponseModel(new_user, "user added successfuuly")


@router.get("/", response_description="all users data retrieved")
async def get_all_users():
    users = await retrieving_all_users()
    if users:
        return ResponseModel(users, "all user data retrieved successfully")
    return ResponseModel(users, "empty list returned")


@router.get("/{id}", response_description="user data retrieved with matching id")
async def get_one_user(id):
    user = await retrieving_one_user(id)
    if user:
        return ResponseModel(user, "user data retrieved with matching id")
    return ErrorResponseModel("An error occured", 404, "user does not exist")


@router.put("/{id}")
async def updating_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await updating_one_user(id, req)
    if updated_user:
        return ResponseModel(
            f"user with ID: {id} name update is successful",
            "user name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


@router.delete("/{id}", response_description="user data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await deleting_one_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )