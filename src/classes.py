from snapchat_bots import SnapchatBot


class WebkomStoryBot(SnapchatBot):
    def on_snap(self, sender, snap):
        self.post_story(snap)

    def on_friend_add(self, friend):
        self.add_friend(friend)

    def on_friend_delete(self, friend):
        self.delete_friend(friend)
