import sqlite3

from snapchat_bots import SnapchatBot
from config import DATABASE


class WebkomStoryBot(SnapchatBot):
    def __init__(self, username, password, use_auth=False):
        super(WebkomStoryBot, self).__init__(username, password)
        self.use_auth = use_auth

    def on_snap(self, sender, snap):
        self.post_story(snap)

    def on_friend_add(self, friend):
        if self.use_auth and not self.is_user_registered(friend):
            return
        self.add_friend(self, friend)

    def is_user_registered(self, username):
        db = sqlite3.connect(DATABASE)
        registered_user = db.execute("SELECT username FROM users WHERE username=?", [username]).fetchone()
        db.close()
        return registered_user is None
