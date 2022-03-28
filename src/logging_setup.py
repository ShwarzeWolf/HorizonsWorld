import logging
import os
from logging import Handler, LogRecord

import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_API_KEY = os.getenv("BOT_API_KEY")
CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(
    format="%(asctime)s => %(filename)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logs.txt",
    level=logging.INFO
)

main_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")

# All logs from INFO level we will write to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(main_formatter)

# All ERROR and CRITICAL errors we will write to another file
file = logging.FileHandler(filename="important_logs.txt")
file.setLevel(logging.ERROR)
file.setFormatter(main_formatter)


# And also, to telegram chat via special handler
class TelegramBotHandler(Handler):
    """Handler to send telegram messages using bot"""
    def __init__(self, api_key: str, chat_id: str):
        super().__init__()
        self.api_key = api_key
        self.chat_id = chat_id

    def emit(self, record: LogRecord):
        """Sends message to chat specified in .env file"""
        bot = telebot.TeleBot(self.api_key)

        bot.send_message(
            self.chat_id,
            self.format(record)
        )


telegram = TelegramBotHandler(BOT_API_KEY, CHAT_ID)
telegram.setLevel(logging.ERROR)
telegram.setFormatter(main_formatter)


# Creating filter
class DrawFilter(logging.Filter):
    """Base class to filter whether or not message should be logged """

    def filter(self, record):
        """Returns False if battle finished with a draw"""
        return not (record.msg.startswith("Battle") and record.msg.endswith("0"))


# Getting root logger
root_logger = logging.getLogger("")

# Adding handlers and filters to the root logger
root_logger.addHandler(console)
root_logger.addHandler(file)
root_logger.addHandler(telegram)

root_logger.addFilter(DrawFilter())
