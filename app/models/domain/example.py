# -*- coding: utf-8 -*-


from pymongo import IndexModel

from app.core.fastapi_motor import ASCENDING, BaseModel


class ExampleModel(BaseModel):
    __coll__: str = "test"

    field: str

    @staticmethod
    async def init_index():
        await ExampleModel.create_indexes(
            [
                IndexModel(
                    [("field", ASCENDING)],
                )
            ]
        )
