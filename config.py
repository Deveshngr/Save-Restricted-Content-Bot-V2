# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24157406"))
API_HASH = getenv("API_HASH", "e2d8ef8ae57b44949e591817291cdd4f")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7473233654").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://nagardeveshjpr:vDBSHxlkeAfVAWs8@cluster0.slvhm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002205849619")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002175174130"))
