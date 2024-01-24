from panther.db.connection import redis

from cache.keys import OTP_KEY
from core.configs import OTP_EXP_SECOND


# # # OTP
def set_otp(phone_number: str, otp: int):
    redis.set(OTP_KEY.format(phone_number), otp, ex=OTP_EXP_SECOND)


def get_otp(phone_number: str) -> str:
    otp = redis.get(OTP_KEY.format(phone_number)) or b""
    return otp.decode()


def remove_otp(phone_number: str):
    redis.delete(OTP_KEY.format(phone_number))
