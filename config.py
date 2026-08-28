from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "24401235"))
    API_HASH = getenv(
        "API_HASH",
        "149f7e13d7d861b27cffc3ab1fd52b22",
    )

    ARQ_API_KEY = getenv(
        "ARQ_API_KEY",
        "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ",
    )

    SPAMWATCH_API = getenv("SPAMWATCH_API", None)

    TOKEN = getenv(
        "TOKEN",
        "8961546223:AAFgl7Ls8aPqH-E-TWNoU_ORNfwTmct5L64",
    )

    OWNER_ID = int(getenv("OWNER_ID", "7255612720"))
    OWNER_USERNAME = getenv(
        "OWNER_USERNAME",
        "Rohith_offcl",
    )

    SUPPORT_CHAT = getenv(
        "SUPPORT_CHAT",
        "AbishnoiMF",
    )

    LOGGER_ID = int(
        getenv("LOGGER_ID", "-1002747283382")
    )

    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://avineyjr004_db_user:0JhozZMlPXZshsBp@cluster0.qtqaact.mongodb.net/?appName=Cluster0",
    )

    DB_NAME = getenv(
        "DB_NAME",
        "PriyankaRobot",
    )

    REDIS_URL = getenv(
        "REDIS_URL",
        "redis-cli --tls -u redis://default:gQAAAAAAAtoaAAIgcDE2OGY2ZTM4MDM2ZTA0NTQyYjA4NTdhYjk1ZjBlODIxNg@holy-halibut-186906.upstash.io:6379",
    )

    # PostgreSQL is optional.
    # MongoDB remains the main database configured above.
    DATABASE_URL = getenv("DATABASE_URL", "postgresql://postgres:KaiPulla@009@db.wonzoqheqdpcltqgfqrd.supabase.co:5432/postgres")

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
