from app.core import logger
from app.core.config import DATABASE_URL, MRS_READ_CONCERN, MRS_WRITE_CONCERN
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import ReadPreference
from pymongo.write_concern import WriteConcern


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to %s", DATABASE_URL)

    app.state.mongodb_client = AsyncIOMotorClient(DATABASE_URL)
    app.state.db = app.state.mongodb_client.get_default_database(
        read_concern=ReadConcern(MRS_READ_CONCERN),
        write_concern=WriteConcern(w=MRS_WRITE_CONCERN),
        read_preference=ReadPreference.PRIMARY_PREFERRED
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    app.state.mongodb_client.close()

    logger.info("Connection closed")
