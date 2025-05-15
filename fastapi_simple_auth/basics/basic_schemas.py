from pydantic import BaseModel


class BasicLoginSchema(BaseModel):
    login: str
    password: str


class BasicGetUserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str

