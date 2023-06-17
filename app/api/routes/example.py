# -*- coding: utf-8 -*-


from fastapi import APIRouter, exceptions, status
from fastapi.requests import Request

from app.core import logger
from app.models.domain.example import ExampleModel
from app.models.schemas.example import ExampleData, ExampleInResponse

router = APIRouter()


@router.get("/", response_model=ExampleInResponse, name="index")
async def on_example(request: Request):
    logger.info("Example start..")
    logger.info(request.url)
    try:
        # coll = request.app.state.db.test
        # result: Example = await coll.find_one({})
        # or
        result = await ExampleModel.find_one({})
    except Exception as e:
        logger.error(e)
        raise exceptions.HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=type(e).__name__
        )
    else:
        if result is None:
            logger.error("Not data..")
            raise exceptions.HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not data"
            )
    logger.info(result)
    return ExampleInResponse(data=ExampleData(field="field"))


@router.post("/", response_model=ExampleInResponse, name="session")
async def on_example_session(request: Request):
    logger.info("Example start..")
    # Session
    try:
        async with await request.app.state.motor_client.start_session() as s:
            async with s.start_transaction():
                # coll = request.app.state.db.test
                # await coll.insert_one({"test": "sessionInsert2"}, session=s)
                # await coll.insert_one({"_id": 1, "test": "sessionInsert"}, session=s)
                # or
                await ExampleModel.insert_one({"test": "sessionInsert2"}, session=s)
                await ExampleModel.insert_one(
                    {"_id": 1, "test": "sessionInsert"}, session=s
                )
    except Exception as e:
        raise exceptions.HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=type(e).__name__
        )
    return ExampleInResponse(data=ExampleData(field="field"))
