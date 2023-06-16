from app.core import logger
from app.core.config import (DATABASE_URL, MAX_CONNECTIONS_COUNT,
                             MIN_CONNECTIONS_COUNT)
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to %s", DATABASE_URL)

    app.state.mongodb_client = AsyncIOMotorClient(DATABASE_URL)
    app.state.db = app.state.mongodb_client.get_default_database()

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    app.state.mongodb_client.close()

    logger.info("Connection closed")
