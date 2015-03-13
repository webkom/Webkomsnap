from src import bot, server
from config import USERNAME, PASSWORD


if __name__ == "__main__":
    server.run()
    webkom_bot = bot.WebkomStoryBot(USERNAME, PASSWORD, use_auth=True)
    webkom_bot.listen()
