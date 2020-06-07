import jwt


# constants
token_expected = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'
ALGORITHM_HS256 = 'HS256'
ERRO_TOKEN_EXPIRED = {"Erro": "Token Expirado"}
ERRO = {"error": 2}


def create_token(data: dict, secret: str) -> bytes:
    return jwt.encode(data, secret, algorithm=ALGORITHM_HS256)


def verify_signature(token: bytes) -> dict:
    try:
        return jwt.decode(token, "acelera", algorithms=ALGORITHM_HS256)
    except jwt.ExpiredSignatureError:
        return ERRO_TOKEN_EXPIRED
    except jwt.InvalidTokenError:
        return ERRO
