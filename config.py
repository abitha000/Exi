from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 24401235))
    API_HASH = getenv("API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "8961546223:AAFgl7Ls8aPqH-E-TWNoU_ORNfwTmct5L64")
    OWNER_ID = int(getenv("OWNER_ID", 7255612720)
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Rohith_offcl")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "AbishnoiMF")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002747283382"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://avineyjr004_db_user:0JhozZMlPXZshsBp@cluster0.qtqaact.mongodb.net/?appName=Cluster0",
    )
    DB_NAME = getenv("DB_NAME", "PriyankaRobot")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
