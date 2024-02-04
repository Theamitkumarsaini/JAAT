import os

API_ID = API_ID = 15052451

API_HASH = os.environ.get("API_HASH", "dbf8fdfc66d7a1a9bf359c036409aa14")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5115275139:AAEJwqeGo0RmycATNb-1gBxUm9sRZYFXJlQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1181522124))

LOG = -1001827442000

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1181522124").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



