from pydantic import BaseModel, Field


class User2(BaseModel):
    username: str = Field(max_length=10, min_length=2,
                          regex="^[A-Za-z0-9_-]+$")
    password: str = Field(max_length=10, min_length=2,
                          regex="^[A-Za-z0-9_-]+$")
    email: str = Field(max_length=10, min_length=2, regex="^[A-Za-z0-9_-]+$")
