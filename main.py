from src import bot
from config import USERNAME, PASSWORD


if __name__ == "__main__":
    webkom_bot = bot.WebkomStoryBot(USERNAME, PASSWORD, use_auth=True)
    webkom_bot.listen()
