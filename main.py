from src.bot import WebkomStoryBot
from config import USERNAME, PASSWORD


if __name__ == "__main__":
    webkom_bot = WebkomStoryBot(USERNAME, PASSWORD, use_auth=True)
    webkom_bot.listen()
