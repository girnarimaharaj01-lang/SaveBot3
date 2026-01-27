# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29777466"))
API_HASH = getenv("API_HASH", "a04b3df726520026f207079aec2f9879")
BOT_TOKEN = getenv("BOT_TOKEN", "8031981205:AAGz3oAzc7hvRHViOirPutAJeiP3t4lvu40")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8399557684").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://girnarimaharaj01_db_user:KsxBY4eoUBwRKXXw@cluster0.6firafk.mongodb.net/?appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003164986113")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003164986113"))
