import logging

# from app.core.logging import InterceptHandler
from starlette.config import Config
from starlette.datastructures import Secret

# import sys


API_PREFIX = "/api"

VERSION = "0.0.0"

config = Config(".env")

PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPIBase")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_URL: str = config("DB_CONNECTION", cast=str,
                           default="mongodb://localhost:27017/fastapi")
# MONGODB Repilca Set Configuration
MRS_READ_CONCERN: str = config("MRS_READ_CONCERN", default="majority")
MRS_WRITE_CONCERN: str = config("MRS_WRITE_CONCERN", default="majority")

MAX_CONNECTIONS_COUNT: int = config(
    "MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config(
    "MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.basicConfig(
    level=LOGGING_LEVEL,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(PROJECT_NAME)
