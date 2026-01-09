#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22484497"))
API_HASH = environ.get("API_HASH", "c38cb053916c47a97590c244663cbaef")
BOT_TOKEN = environ.get("BOT_TOKEN", "8243552643:AAFLbmt2AShiB7ESpK84yAI44EgkNd51Tno")

OWNER = int(environ.get("OWNER", "6252997817"))
CREDIT = environ.get("CREDIT", "ᴹᴿ🌿⃝🅺ιʟͥʟͣᴇᷟʀ✍࿐ཽ༵")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6478217960,6252997817').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6478217960,6252997817').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


