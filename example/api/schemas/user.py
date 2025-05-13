from pydantic import BaseModel


class CustomGetUserSchema(BaseModel):
    id: int
    full_name: str
    phone: str
    username: str
    email: str
    passport_number: str
    insurance_number: str
