import sqlite3

from flask import Flask, request, jsonify, abort
from Webkomsnap.config import DATABASE

app = Flask(__name__)
print(DATABASE)

@app.route('/create', methods=["POST"])
def recognize_user():
    if not request.json or not 'username' in request.json:
        abort(400)


if __name__ == "__main__":
    app.run()
