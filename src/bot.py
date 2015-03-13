import sqlite3
import logging

from snapchat_bots import SnapchatBot
from config import DATABASE, SNAP_LOG, LOG_FORMAT

logging.getLogger(name="requests").setLevel(logging.WARN)
logging.root.removeHandler(logging.root.handlers[0])
logging.basicConfig(filename=SNAP_LOG, format=LOG_FORMAT, level=logging.DEBUG)
logger = logging.getLogger()


class WebkomStoryBot(SnapchatBot):
    def __init__(self, username, password, use_auth=False):
        super(WebkomStoryBot, self).__init__(username, password)
        self.use_auth = use_auth

    def log(self, message, level=logging.INFO):
        pass

    def no_spam_log(self, message, level=logging.INFO):
        logger.log(level, message)

    def on_snap(self, sender, snap):
        try:
            self.post_story(snap)
            self.no_spam_log("Received a snap from {}.".format(snap.sender))
        except ValueError:
            self.no_spam_log("Received invalid data.", level=logging.ERROR)

    def on_friend_add(self, friend):
        if self.use_auth and not self.user_is_registered(friend):
                self.no_spam_log("User {} is not in the recognized users database, not accepting friend request".format(friend))
                return
        self.add_friend(friend)
        self.no_spam_log("Added {} as a friend.".format(friend))

    def is_user_registered(self, username):
        db = sqlite3.connect(DATABASE)
        registered_user = db.execute("SELECT username FROM users WHERE username=?", [username]).fetchone()
        db.close()
        return bool(registered_user)
