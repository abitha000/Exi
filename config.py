from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "YOUR_API_ID"))
    API_HASH = getenv("API_HASH", "YOUR_API_HASH")

    ARQ_API_KEY = getenv("ARQ_API_KEY", "")
    SPAMWATCH_API = getenv("SPAMWATCH_API", None)

    TOKEN = getenv("TOKEN", "YOUR_BOT_TOKEN")

    OWNER_ID = int(getenv("OWNER_ID", "YOUR_OWNER_ID"))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Rohith_offcl")

    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "AbishnoiMF")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002747283382"))

    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "YOUR_MONGODB_URI",
    )

    DB_NAME = getenv("DB_NAME", "PriyankaRobot")

    REDIS_URL = getenv(
        "REDIS_URL",
        "YOUR_REDIS_URL",
    )

    DATABASE_URL = getenv("DATABASE_URL", None)

    # PostgreSQL compatibility
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace(
            "postgres://",
            "postgresql://",
            1,
        )


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
