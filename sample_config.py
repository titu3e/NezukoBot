from dotenv import load_dotenv
from os import environ,path
if path.exists("config.env"):
    load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN", "5016713832:AAFanQaM9w7R6H0KvCW8LoxDTK5-yu1ui9E")
API_ID = int(environ.get("API_ID", 8626831))
API_HASH = environ.get("API_HASH", "db23330a6edf4a517ee186b35cedec71")
SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "1593338093").split()]
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", -1001598625668))
GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", -1001598625668))
MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", -1001598625668))
WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", 300))
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://dbmab:eUtbAuei6mpLoinz@cluster0.r2c3m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
ARQ_API_URL = environ.get("ARQ_API_URL", "https://thearq.tech")
ARQ_API_KEY = environ.get("ARQ_API_KEY", AEWDWZ-AUZSMK-DWRYWB-VUBMGC-ARQ)
RSS_DELAY = int(environ.get("RSS_DELAY", 300))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/titu3e/NezukoBot.git")
