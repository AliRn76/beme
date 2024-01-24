from panther.serializer import ModelSerializer
from pydantic import Field, field_validator

import cache
from core.configs import OTP_LEN
from user.models import User


class SendOTPSerializer(metaclass=ModelSerializer, model=User):
    fields = ["phone_number"]


class LoginSerializer(SendOTPSerializer):
    otp: str = Field(min_length=OTP_LEN, max_length=OTP_LEN)

    @field_validator("otp")
    def validate(cls, otp, fields):
        phone_number = fields.data["phone_number"]
        if otp == cache.get_otp(phone_number):
            cache.remove_otp(phone_number)
            return otp
        raise ValueError("OTP is not valid.")
