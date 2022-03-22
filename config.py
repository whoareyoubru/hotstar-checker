from dotenv import load_dotenv
import os

if os.path.exists("dangernetwork.env"):
    load_dotenv("dangernetwork.env")
else:
    load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_NAME = getenv("OWNER_NAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
CHANNEL = getenv("SUPPORT_CHANNEL")

