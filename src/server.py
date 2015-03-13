import sqlite3

from flask import Flask, request, jsonify, g
from config import TOKEN, DATABASE

app = Flask(__name__)


@app.before_request
def open_db_connection():
    g.db = sqlite3.connect(DATABASE)


@app.teardown_appcontext
def close_db_connection(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/create', methods=["POST"])
def auth_user():
    if not request.json or 'username' not in request.json or 'token' not in request.json:
        return jsonify(error="Invalid json. Expected username and token fields"), 400

    token = request.json.get('token')
    username = request.json.get('username')

    if token == TOKEN:
        exists = g.db.execute("SELECT username FROM users WHERE username = ?", [username]).fetchone()
        if exists is not None:
            return jsonify(error="A user with that username is already registered"), 400
        g.db.execute("INSERT INTO users ('username') VALUES (?)", [username])
        g.db.commit()
        return jsonify(username=username), 201
    else:
        return jsonify(error="Invalid token."), 403

if __name__ == "__main__":
    app.run()
