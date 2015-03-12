from __future__ import absolute_import

from src.webkomstory.classes import WebkomStoryBot
from config import USERNAME, PASSWORD


if __name__ == "__main__":
    bot = WebkomStoryBot(USERNAME, PASSWORD)
    bot.listen()
