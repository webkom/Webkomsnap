import sqlite3
import logging

from flask import Flask, request, jsonify, g
from config import TOKEN, DATABASE, SERVER_LOG, LOG_FORMAT

app = Flask(__name__)
logging.getLogger(name="werkzeug").setLevel(logging.FATAL)
logging.basicConfig(filename=SERVER_LOG, format=LOG_FORMAT, level=logging.DEBUG)
logger = logging.getLogger()

@app.before_request
def open_db_connection():
    g.db = sqlite3.connect(DATABASE)


@app.teardown_appcontext
def close_db_connection(exception):
    if hasattr(g, 'db'):
        g.db.close()


def log(message, level=logging.INFO):
    logger.log(level, message)


@app.route('/create', methods=["POST"])
def auth_user():
    if not request.json or 'username' not in request.json or 'token' not in request.json:
        log("Received an invalid request")
        return jsonify(error="Invalid json. Expected username and token fields"), 400

    token = request.json.get('token').strip()
    username = request.json.get('username').strip()

    if token == TOKEN:
        exists = g.db.execute("SELECT username FROM users WHERE username = ?", [username]).fetchone()
        if exists is not None:
            log("User {} attempted to re-register".format(username))
            return jsonify(error="A user with that username is already registered"), 400
        g.db.execute("INSERT INTO users ('username') VALUES (?)", [username])
        g.db.commit()
        log("Added user {} to recognized users.".format(username))
        return jsonify(username=username), 201
    else:
        log("Received an unauthorized request from {}".format(username))
        return jsonify(error="Invalid token."), 403

if __name__ == "__main__":
    app.run()
