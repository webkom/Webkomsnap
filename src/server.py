import sqlite3
from flask import Flask, request, jsonify, abort


class AuthServer:
    app = Flask(__name__)

    def __init__(self, token):
        self.token = token

    def run(self):
        self.app.run()

    @app.route('/create', methods=["POST", "GET"])
    def auth_user():
        if not request.json or 'username' not in request.json or 'token' not in request.json:
            abort(400)
       
        token = request.json.get('token')
        username = request.json.get('username')
        if token == self.token:


server = AuthServer("123")
server.run()
