from argparse import ArgumentParser
from snapchat_bots import SnapchatBot


class ReflectorBot(SnapchatBot):
    def on_snap(self, sender, snap):
        self.send_snap([sender], snap)

    def on_friend_add(self, friend):
        self.add_friend(friend)

    def on_friend_delete(self, friend):
        self.delete_friend(friend)

if __name__ == '__main__':
    parser = ArgumentParser("Reflector Bot")
    parser.add_argument('-u', '--username', required=True, type=str, help="Username of the account to run the bot on")
    parser.add_argument('-p', '--password', required=True, type=str, help="Password of the account to run the bot on")

    args = parser.parse_args()

    bot = ReflectorBot(args.username, args.password)
    bot.listen(timeout=5)
