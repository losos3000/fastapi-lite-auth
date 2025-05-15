# FastAPI Simple Auth
This is a login/password authentication module that can be quickly and easily integrated into your project.
JWT token is used as the authentication method. It is recommended to use the module in small projects and pet projects.

To add the module to your project, you need to:

1. Install the module
2. Override the `get_user` method in `auth_manager`
3. Override the user schema and model in `auth_manager` if they differ from yours
4. Specify which fields in the user model represent the login and password 

More detailed installation and configuration instructions can be found in the `Installation` section.

Based on [AuthX](https://github.com/yezz123/authx)


---

## Installation
### Installing the module
Clone dir `fastapi-simple-auth` to your project.

~~Install module~~
~~`pip install fastapi-simple-auth`~~
The module is currently being prepared for publishing to `PyPI`.

### Module integration
In the folder containing your API routers (usually `routers/`), create a file named `auth.py`.
Import the necessary components and create the API router:
`auth.py`:
```python
from fastapi import APIRouter
from fastapi_simple_auth import auth_config, auth_router, auth_manager

auth_config.authx_ready()

router = APIRouter()
router.include_router(
    router=auth_router
)
```

The `auth_config.authx_ready()` function configures the AuthX object. You should call it after modifying any `auth_config` settings. 

### Basic module configuration
To make the module work, you need to do a few things:

#### 1. Override the user model and schema.
The model is an ORM-oriented class.
The schema is a class that describes the data the API will return.

By default, they look like this:
```python
from pydantic import BaseModel

class BasicGetUserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str
    
class BasicUserModel:
    id: int
    name: str
    email: str
    username: str
    password: str
```

Example of overriding the user model and schema:
```python
from pydantic import BaseModel
from fastapi_simple_auth import auth_config

class CustomGetUserSchema(BaseModel):
    id: int
    full_name: str
    phone: str
    username: str
    email: str
    passport_number: str
    insurance_number: str

class CustomUserModel:
    id: int
    full_name: str
    phone: str
    username: str
    email: str
    passport_number: str
    insurance_number: str
    password: str
    
auth_config.models_config.UserModel = CustomUserModel
auth_config.schemas_config.GetUserSchema = CustomGetUserSchema
```

#### 2. Define the user retrieval method.
This is a function that should find a user record in your database using the field used as login.
Requirements:
- The function must accept a `login` argument of type `str`
- It must return an instance of the user model described above or `None` if not found

Example override:
```python
import sqlite3
from fastapi_simple_auth import auth_config, auth_manager

def get_user_by_login( login: str | None = None) -> auth_config.models_config.UserModel | None:
    conn = sqlite3.connect("./db.db")
    select = conn.execute(f"SELECT * FROM user WHERE email = ?", (login,))
    res = select.fetchone()

    if res is None:
        return None

    user_model = auth_config.models_config.UserModel()
    user_model.id = res[0]
    user_model.full_name = res[1]
    user_model.username = res[2]
    user_model.email = res[3]
    user_model.password = res[4]

    return user_model

auth_manager.get_user = get_user_by_login
```

#### 3. Configure login and password fields
By default, `username` and `password` fields are used.
Example configuration:
```python
from fastapi_simple_auth import auth_config

auth_config.login_config.login_field_name = "email"
auth_config.login_config.password_field_name = "password"
auth_config.authx_ready()
```

### Additional configuration
#### 1. Define a password hashing function (if passwords are stored hashed in your DB)
This function is used to hash the incoming password for comparison.
Requirements:
- Must accept a `data` argument of type `str`
- Must return a `str` hash

Example:
```python
from hashlib import sha256
from fastapi_simple_auth import auth_manager

def hash(data: str) -> str:
    return sha256(data.encode()).hexdigest()

auth_manager.hash = hash
```

#### 2. Configure the secret key
The secret key is used to sign the JWT token.
It should be stored in environment variables.
By default, it’s generated from the current datetime.

Example override:
```python
import os
from fastapi_simple_auth import auth_config

auth_config.token_config.secret_key = os.getenv("AUTH_SECRET")
auth_config.authx_ready()
```

#### 3. Configure cookie parameters
Here’s how to configure cookies and their default values:
```python
from fastapi_simple_auth import auth_config

auth_config.cookie_config.cookie_name = "auth_token"
auth_config.cookie_config.cookie_httponly = False
auth_config.cookie_config.cookie_secure = False
auth_config.cookie_config.cookie_samesite = "lax"
auth_config.cookie_config.cookie_max_age = 3600
auth_config.cookie_config.cookie_path = "/"
auth_config.cookie_config.cookie_domain = None
auth_config.cookie_config.cookie_expires = None
auth_config.authx_ready()
```

### Example integration
You can check out the example app in the `example` directory.
Its configuration is described in `example/api/routers/auth.py`.

---

## Requirements
```shell
pip install -r requirements.txt
```
or
```shell
pip install "fastapi[standard]"
pip install authx 
```

## Start Example
### API
```shell
python3 -m example.api.main
```