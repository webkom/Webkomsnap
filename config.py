import os
import logging

USERNAME = "webkom_story"
PASSWORD = "78CuhGdu"
DATABASE = os.path.join(os.path.abspath(os.curdir), "sqlite_db")
TOKEN = "QCNct7Qb9JcNkqF" # <- Top secret.
LOG = os.path.join(os.path.abspath(os.curdir), "log.log")
logging.basicConfig(filename=LOG, level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
