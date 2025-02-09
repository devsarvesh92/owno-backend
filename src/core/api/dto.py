"""
Data Transfer Object (DTO) is a design pattern used to transfer data between software application subsystems.
"""

from pydantic import BaseModel, constr


class UserRegisterRequest(BaseModel):
    phone_number: constr(pattern=r"^\+?1?\d{9,15}$")


class UserRegisterResponse(BaseModel):
    phone_number: str
    user_id: str
    message: str
    otp: str = None
