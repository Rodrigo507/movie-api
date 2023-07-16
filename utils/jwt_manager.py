from jwt import encode, decode
from decouple import config


def create_token(data: dict):
    token: str = encode(payload=data, key=config(
        'SECREAT_KEY'), algorithm='HS256')
    return token


def validate_token(token: str):
    try:
        payload = decode(token, key=config(
            'SECREAT_KEY'), algorithms=['HS256'])
        return payload
    except:
        return False
