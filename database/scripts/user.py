
users = [
    {
        "id": 1,
        "username": "losos3000",
        "password": "test",
    },
    {
        "id": 2,
        "username": "nagibator",
        "password": "test",
    },
    {
        "id": 0,
        "username": "admin",
        "password": "admin",
    }
]


def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return {"id": user["id"], "username": user["username"]}

    return None


async def get_user_id(user_username) -> int | None:
    for user in users:
        if user["username"] == user_username:
            return user["id"]

    return None