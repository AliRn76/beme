from panther import status
from panther.app import GenericAPI
from panther.authentications import JWTAuthentication
from panther.request import Request
from panther.response import Response

import cache
from core.configs import OTP_EXP_SECOND
from services.mediana import Mediana
from user.models import User
from user.serializers import (
    LoginSerializer,
    SendOTPSerializer,
)
from user.utils import generate_otp


class SendOTPAPI(GenericAPI):
    input_model = SendOTPSerializer

    def post(self, request: Request):
        phone_number = request.validated_data.phone_number
        otp = generate_otp()
        cache.set_otp(phone_number=phone_number, otp=otp)
        Mediana.send_otp(recipient=phone_number, otp=otp)
        data = {"detail": "OTP sent successfully.", "otp_exp": OTP_EXP_SECOND}
        return Response(data=data, status_code=status.HTTP_202_ACCEPTED)


class LoginAPI(GenericAPI):
    input_model = LoginSerializer

    def post(self, request: Request):
        phone_number = request.validated_data.phone_number
        _, user = User.find_or_insert(phone_number=phone_number)
        user.update_last_login()
        access = JWTAuthentication.encode_jwt(user_id=user.id)
        refresh = JWTAuthentication.encode_refresh_token(user_id=user.id)
        return Response(
            data={"access": access, "refresh": refresh}, status_code=status.HTTP_200_OK
        )
