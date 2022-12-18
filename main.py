from flask import Flask, request
from modules.twitch import get_twitch_user

app = Flask(__name__)

@app.route('/v1/users', methods=['GET'])
def get_twitch_users():
    user = request.args.get('user')
    return get_twitch_user(user)

@app.route('/v1/users', methods=['DELETE'])
def delete_twitch_users():
    pass

if __name__ == '__main__':
    app.run()
