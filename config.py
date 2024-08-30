# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27868202"))
API_HASH = getenv("API_HASH", "bf6d423ddc4a4999f09750872bdc2497")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6497588567").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://adultverse04:adultverse04@adultverse04.wpltj.mongodb.net/?retryWrites=true&w=majority&appName=adultverse04")
LOG_GROUP = getenv("LOG_GROUP", "-1002224815385")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002232787597"))
