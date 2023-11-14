import os

API_ID = API_ID = 8006372

API_HASH = os.environ.get("API_HASH", "f878ef2fd1044167b7d8ab23320e1eda")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6505335502:AAG_eIVz0iC7E5GWp8Y-k00kYaOIEQCuKao")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1924424042))

LOG = -1001812808410

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1924424042").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


