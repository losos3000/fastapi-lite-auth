import os
import logging
from dotenv import load_dotenv


#SYSTEM CONFIG
PROJECT_NAME = "authentication_module"
PROJECT_VERSION = "0.1"


#MAIN DIRECTORY CONFIG
#WORK_DIRECTORY = f"/opt/{PROJECT_NAME}/"
WORK_DIRECTORY = f"/Users/losos3000/Desktop/Projects/01_MY/Authentication_Module/"

#MODULE DIRECTORY CONFIG
# BOT_DIRECTORY = f"{PROJECT_DIRECTORY}/bot"


#ENV CONFIG
ENV_NAME = ".env"
ENV_PATH = f"{WORK_DIRECTORY}/{ENV_NAME}"
load_dotenv(ENV_PATH)


#TOKENS
# BOT_TOKEN = os.getenv("BOT_TOKEN")


#LOGS CONFIG
LOG_LEVEL=logging.DEBUG
LOG_NAME = f"{PROJECT_NAME}.log"
LOG_DIRECTORY = f"{WORK_DIRECTORY}/logs"
LOG_PATH = f"{LOG_DIRECTORY}/{LOG_NAME}"
LOG_FORMAT = "%(asctime)s %(levelname)s\t: [%(filename)s] (Line: %(lineno)d) %(message)s"
LOG_DATEFMT = "%Y-%m-%d %I:%M:%S"
LOG_ENCODING = "utf-8"
LOG_FILEMODE = "w"


#DB CONFIG
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
