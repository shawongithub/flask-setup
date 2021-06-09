from datetime import datetime,timedelta
import jwt
from flask import request, jsonify
from functools import partial, wraps

class TokenProvider:
    def __init__(self):
        self.jwt_time_validity_in_seconds = 7200
        self.secret_key = '#123Secret'

    def provide(self, user_pk, all_role):

        payload = {
            "id":"{}".format(user_pk),
            "roles":all_role,
            "exp":datetime.utcnow()+timedelta(seconds=self.jwt_time_validity_in_seconds)
        }

        jwt_token = jwt.encode(payload,self.secret_key)
        return 1, (jwt_token.decode('utf-8'))

    def get_token_value(self, token):
        try:
            decoded_token = jwt.decode(token, self.secret_key)
            user_pk = decoded_token.get('id' , None)
            roles = decoded_token.get('roles', None)
            return True, user_pk, roles
        except Exception as e:
            print(str(e))
            return False, '', ''


def authenticate_appuser():
    if 'X-Jwt-Token' in request.headers.keys():
        jwt_token = request.headers.get('X-Jwt-Token').replace('Bearer ', '')
        token_provider = TokenProvider()
        sts, app_user, roles = token_provider.get_token_value(jwt_token)

        return sts, app_user, roles

def admin_policy(func, role):
    @wraps(func)
    def authorization(*args, **kwargs):
        if not 'X-Jwt-Token' in request.headers.keys():
            return jsonify(error='no authentication bearer')
        
        jwt_token = request.headers.get('X-Jwt-Token').replace('Bearer ', '')
        token_provider = TokenProvider()
        sts, app_user, roles = token_provider.get_token_value(jwt_token)
        if sts:
            if role not in roles:
                return jsonify(error="access denied")
        else:
            return jsonify(error="invalid token or expired")
        return func(*args, **kwargs)
    return authorization

author = partial(admin_policy, role="author")
editor = partial(admin_policy, role="editor")