from flask import Flask, g, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import re
from deal_token import Token
from mysql import Count

app = Flask(__name__)
CORS(app, supports_credentials=True)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user_id = re.sub(r'^"|"$', '', username)
    user_id = Token().verify_token(user_id)
    if not user_id:
        user_id = Count().get_user(username, password)
        if not user_id:
            return False
    g.user_id = user_id.get('user_id')
    return True


@app.route('/login')
@auth.login_required()
def login():
    token = Token().generate_token(g.user_id)
    return jsonify({'token': token.decode()})


@app.route('/index')
@auth.login_required
def index():
    return 'index'


if __name__ == '__main__':
    app.run()



