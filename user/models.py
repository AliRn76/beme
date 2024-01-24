from datetime import date, datetime
from typing import Literal

from panther.db import Model
from panther.file_handler import Image
from pydantic import EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class User(Model):
    phone_number: PhoneNumber
    first_name: str = Field(default="", max_length=64)
    last_name: str = Field(default="", max_length=64)
    profile_picture: Image | None = Field(default=None)
    gender: Literal["male", "female"] | None = Field(default=None)
    birth_date: date | None = Field(default=None)
    email: EmailStr | None = Field(default=None)
    last_login: datetime | None = None

    def update_last_login(self) -> None:
        self.update(last_login=datetime.now())


class Host(Model):
    user_id: str
    sheba_number: str | None = Field(default=None)
