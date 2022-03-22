import re
import sys
import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("dangernetwork.env"):
    load_dotenv("dangernetwork.env")
else:
    load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_NAME = getenv("OWNER_NAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")

