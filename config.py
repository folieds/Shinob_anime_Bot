# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7193814472:AAGA2mA_2ESVtVGNySJW5oiacAjnm4OUUIg")
#Your API ID from my.telegram.org --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "24371796"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002118745640"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "1439890119"))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "-1002097138409")

#Port
PORT = os.environ.get("PORT", "8030")

#Database --⚠️ REQUIRED--
DB_URL = os.environ.get("DB_URL", "mongodb+srv://AnimeRavenBots:AnimeRavenBots@animeravenbots.huekk.mongodb.net/?retryWrites=true&w=majority&appName=DevilFruitBot")
DB_NAME = os.environ.get("DATABASE_NAME", "DevilFruitBot")

VERIFY_DB = os.environ.get("VERIFY_DB", "mongodb+srv://dattebayo56:dattebayo56@animeravenbots.6wcgy.mongodb.net/?retryWrites=true&w=majority")
DBV_NAME = os.environ.get("VERIFY_DBNAME", "OrewaSanjiiBots")


TOKEN_PIC = os.environ.get("TOKEN_PIC", "https://envs.sh/H2r.jpg")


#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_Download_7x/32")


START_PIC = os.environ.get("START_PIC", "https://envs.sh/H2r.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/H2r.jpg")

                        
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://envs.sh/H2r.jpg")).split() #Required
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
