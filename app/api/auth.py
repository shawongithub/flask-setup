from flask import request, jsonify
from app import app
from app.models import User, Power, Role
from app.utils.authenticator import TokenProvider

@app.route('/api/v1/signup', methods=['POST'])
def user_signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    power = data.get('power')
    try:
        user = User.get_or_create(name=name, email=email)
        power, created = Power.get_or_create(title=power)
        role, created = Role.get_or_create(user=user[0].id, power=power, status=True)
        return jsonify(result='ok')
    except:
        return jsonify(error='error saving user')

@app.route('/api/v1/login', methods=['GET'])
def user_login():
    data = request.get_json()
    email = data.get('email')
    token_provider = TokenProvider()
    try:
        user = User.get_or_none(email=email)
        if user != None:
            roles = Role.select().where(Role.user==user)
            all_role = [role.power.title for role in roles]
            sts, token = token_provider.provide(user.id, all_role)
            if sts:
                return jsonify(jwt=token)
        return jsonify(result='no account exist')
    except Exception as e:
        return jsonify(error=str(e))
        