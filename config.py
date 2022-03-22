from dotenv import load_dotenv

if os.path.exists("my.env"):
    load_dotenv("my.env")
else:
    load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_NAME = getenv("OWNER_NAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
CHANNEL = getenv("SUPPORT_CHANNEL")

