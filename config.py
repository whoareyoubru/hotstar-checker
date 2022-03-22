from dotenv import load_dotenv
import os

if os.path.exists("dangernetwork.env"):
    load_dotenv("dangernetwork.env")
else:
    load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
OWNER_NAME = os.environ.get("OWNER_NAME", None)
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", None)
SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL", None)

