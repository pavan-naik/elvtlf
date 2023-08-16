# telegram_manager.py

from urllib.parse import urlparse
from telegram import Bot, Update, InputFile
from telegram.ext import Updater, MessageHandler, filters, CallbackContext
from telegram.constants import ParseMode
from common import get_logger
logger = get_logger(__name__)

class TelegramManager:
    def __init__(self, bot_token, channel_username):
        self.bot_token = bot_token
        self.channel_username = channel_username
        
    async def send_message(self, message):
        logger.info("Started sending message.")
        bot = Bot(token=self.bot_token)
        await bot.send_message(chat_id=self.channel_username, text=message)
        logger.info(f"Mesasage sent to {self.channel_username}")
        
    async def send_message_with_image(self, image_path_or_url, caption):
        logger.info("Started sending message with image.")
        bot = Bot(token=self.bot_token)

        # Check if the input is a URL or a local path
        if urlparse(image_path_or_url).scheme:
            # Input is a URL
            await bot.send_photo(
                chat_id=self.channel_username,
                photo=image_path_or_url,
                caption=caption,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            # Input is a local path
            with open(image_path_or_url, 'rb') as photo_file:
                await bot.send_photo(
                    chat_id=self.channel_username,
                    photo=InputFile(photo_file),
                    caption=caption,
                    parse_mode=ParseMode.MARKDOWN
                )
        logger.info(f"Mesasage sent to {self.channel_username}")
                

