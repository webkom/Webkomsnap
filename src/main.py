from classes import WebkomStoryBot
from config import username, password


if __name__ == "__main__":
    bot = WebkomStoryBot(username, password)
    bot.listen()
