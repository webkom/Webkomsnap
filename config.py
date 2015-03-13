import os

USERNAME = "webkom_story"
PASSWORD = "78CuhGdu"
DATABASE = os.path.join(os.path.abspath(os.curdir), "sqlite_db")
TOKEN = "QCNct7Qb9JcNkqF" # <- Top secret.
LOG_DIR = os.path.join(os.path.abspath(os.curdir), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
SNAP_LOG = os.path.join(LOG_DIR, "snap.log")
SERVER_LOG = os.path.join(LOG_DIR, "server.log")
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
