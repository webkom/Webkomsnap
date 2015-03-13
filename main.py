from src.bot import WebkomStoryBot
from config import USERNAME, PASSWORD, USE_AUTH


if __name__ == "__main__":
    webkom_bot = WebkomStoryBot(USERNAME, PASSWORD, use_auth=USE_AUTH)
    webkom_bot.listen()
