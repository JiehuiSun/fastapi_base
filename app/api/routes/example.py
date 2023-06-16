# -*- coding: utf-8 -*-


from app.core import logger
from app.models.schemas.example import ExampleInResponse, ExampleData
from fastapi import APIRouter, exceptions, status
from fastapi.requests import Request

router = APIRouter()


@router.post("/", response_model=ExampleInResponse, name="index")
async def on_example(request: Request):
    logger.info("Example start..")
    coll = request.app.state.db["test"]
    try:
        result = await coll.find_one({})
    except Exception as e:
        raise exceptions.HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=type(e).__name__
        )
    else:
        if result is None:
            logger.error("Not data..")
            raise exceptions.HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Not data'
            )
    logger.info(result)
    return ExampleInResponse(
        data=ExampleData(
            field="field"
        )
    )
