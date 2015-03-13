import sqlite3
import logging

from snapchat_bots import SnapchatBot
from config import DATABASE


class WebkomStoryBot(SnapchatBot):
    def __init__(self, username, password, use_auth=False):
        super(WebkomStoryBot, self).__init__(username, password)
        self.use_auth = use_auth

    def on_snap(self, sender, snap):
        try:
            self.post_story(snap)
            logging.info("Received a snap from {}".format(snap.sender))
        except ValueError:
            logging.error("Received invalid data.")

    def on_friend_add(self, friend):
        if self.use_auth and not self.is_user_registered(friend):
            logging.info("User {} is not in the recognized users database, not accepting friend request".format(friend))
            return
        self.add_friend(self, friend)
        logging.info("Added {} as a friend.".format(friend))

    def is_user_registered(self, username):
        db = sqlite3.connect(DATABASE)
        registered_user = db.execute("SELECT username FROM users WHERE username=?", [username]).fetchone()
        db.close()
        return registered_user is None
