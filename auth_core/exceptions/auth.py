from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidPassword2Exception(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Password 2 invalid!"
    default_code = "invalid_password_2"
