
from dotenv import load_dotenv
import os
import re
import asyncio
import argparse
from telegram_manager import TelegramManager  # Updated import

# Load environment variables from .env
load_dotenv('config.env')

def parse_arguments():
    parser = argparse.ArgumentParser(description="Telegram Channel Manager")
    parser.add_argument("--bot_token", default=os.getenv("BOT_TOKEN"), help="Bot token")
    parser.add_argument("--channel_username", default=os.getenv("CHANNEL_USERNAME"), help="Channel username")
    return parser.parse_args()
    
async def main():    
    args = parse_arguments()
    channel_manager = TelegramManager(args.bot_token, args.channel_username)  # Updated class name

    #image_link = "https://m.media-amazon.com/images/I/21eW-Qg1tGL._SL160_.jpg"
    product_link = "https://amzn.to/3OT91KO"
    html_code = '<a href="https://www.amazon.in/Oppo-Wireless-Industry-Composite-Playtime/dp/B0C9Q3TW83?crid=BRR2S7SFM5HD&keywords=oppo+enco+buds+3+pro&qid=1691951805&sprefix=OPPO+Enco+Buds%2Caps%2C343&sr=8-3&linkCode=li3&tag=elevateyour0e-21&linkId=f42478f06ebc1274acc460e69a27b3ea&language=en_IN&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0C9Q3TW83&Format=_SL5000_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=elevateyour0e-21&language=en_IN" ></a><img src="https://ir-in.amazon-adsystem.com/e/ir?t=elevateyour0e-21&language=en_IN&l=li3&o=31&a=B0C9Q3TW83" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'

    # Extract the relative image URL using regular expression
    relative_image_url = re.search(r'src="(.*?)"', html_code).group(1)

    # Construct the full image URL
    full_image_url = f"https:{relative_image_url}"

    message = f"""🎧 *Best Quality Bluetooth Earbuds Deal! **[Oppo Enco Air3 Pro]({product_link})**"""
    
    # Send a message
    await channel_manager.send_message_with_image(full_image_url, message)  # Updated class name
    
    
#     # List channel messages
#     channel_manager.list_channel_messages()  # Updated class name

#     # Stop polling when done
#     channel_manager.stop_polling()
#     messages = [
#         "Message 1",
#         "Message 2",
#         "Message 3",
#         # ... add more messages here
#     ]
#     interval_seconds = 5  # Adjust as needed
#     asyncio.run(manager.schedule_messages(messages, interval_seconds))


if __name__ == "__main__":
    asyncio.run(main())
