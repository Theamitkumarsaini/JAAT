import os

API_ID = API_ID = 20544260

API_HASH = os.environ.get("API_HASH", "a0b00461d3fba22aa186fa648d77787e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6940355682:AAEaTbv9tLz7ZKOEcMJ1HBioIP2goQOdQSY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6389388334))

LOG = -1002051259332

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6389388334").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



