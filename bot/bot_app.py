import telebot

import os
from dotenv import load_dotenv

env_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(env_dir, ".env")

load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv('MY_CHAT_ID')


def bot_inform(msg: str):
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=msg)


# для теста
if __name__ == "__main__":
    bot_inform(msg="привет")
