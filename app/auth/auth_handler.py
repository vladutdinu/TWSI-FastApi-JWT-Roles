import time
from typing import Dict
import os
import jwt
from decouple import config

JWT_SECRET = '5547e593f05c31ce94aaf75ee7d9a0036798c3475154f12c8faa08dc9659d7fd' #os.environ["SECRET"]
JWT_ALGORITHM = "HS256"

def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str, role: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600,
        "role": role
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
