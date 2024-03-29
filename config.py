import os

USE_AUTH = False
USERNAME = "webkom_story"
PASSWORD = "password" # Only one user can be logged in at a time, so if you run main.py on your machine, the one on the server is going to die. Bad idea.
DATABASE = os.path.join(os.path.abspath(os.curdir), "sqlite_db")
TOKEN = "QCNct7Qb9JcNkqF" # <- Top secret.
LOG_DIR = os.path.join(os.path.abspath(os.curdir), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
SNAP_LOG = os.path.join(LOG_DIR, "snap.log")
SERVER_LOG = os.path.join(LOG_DIR, "server.log")
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
