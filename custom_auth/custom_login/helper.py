from random import randint
from kavenegar import *
from custom_auth.settings import KAVENEGAR_API


def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(KAVENEGAR_API)
        params = {
            'receptor': mobile,
            'message': f'your otp is {otp}'
        }
        response = api.sms_send(params)
        print(response)
        print(otp)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000, 9999)
