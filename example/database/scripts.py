import sqlite3
from example.database.database import DB_PATH

from fastapi_lite_auth import auth_config


def get_user_by_login( login: str | None = None) -> auth_config.models_config.UserModel | None:
    conn = sqlite3.connect(DB_PATH)
    select = conn.execute(
        f"SELECT * FROM user WHERE {auth_config.login_config.login_field_name} = ?",
        (login,)
    )

    res = select.fetchone()

    if res is None:
        return None

    user_model = auth_config.models_config.UserModel()
    user_model.id = res[0]
    user_model.full_name = res[1]
    user_model.phone = res[2]
    user_model.username = res[3]
    user_model.email = res[4]
    user_model.passport_number = res[5]
    user_model.insurance_number = res[6]
    user_model.password = res[7]

    return user_model
