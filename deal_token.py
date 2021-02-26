from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature


class Token:
    def __init__(self):
        self.SECRET_KEY = 'abcdefghijklmm'
        self.expiration = 36000

    def generate_token(self, user_id):
        s = Serializer(self.SECRET_KEY, expires_in=self.expiration)
        return s.dumps({'user_code': user_id})

    def verify_token(self, token):
        s = Serializer(self.SECRET_KEY)
        try:
            data = s.loads(token)
            return data
        except SignatureExpired:
            return None
        except BadSignature:
            return None