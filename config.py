from dotenv import load_dotenv

if os.path.exists("my.env"):
    load_dotenv("my.env")
else:
    load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
