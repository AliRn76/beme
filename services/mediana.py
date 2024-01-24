import requests

from core.configs import MEDIANA_KEY


class Mediana:
    URL = "https://api2.ippanel.com/api/v1"
    OTP_PATTERN = "xxx"
    OTP_PATH = "/sms/pattern/normal/send"

    @classmethod
    def _send_sms(cls, path: str, payload: dict):
        requests.post(headers={"apikey": MEDIANA_KEY}, url=cls.URL + path, json=payload)

    @classmethod
    def send_otp(cls, recipient: str, otp: int):
        payload = {
            "code": cls.OTP_PATTERN,
            "sender": "+983000505",
            "recipient": recipient,
            "variable": {"otp": otp},
        }

        print(payload)
        # cls._send_sms(path=cls.OTP_PATH, payload=payload)
