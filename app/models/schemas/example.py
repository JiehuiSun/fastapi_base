# -*- coding: utf-8 -*-


from app.models.schemas import BaseModel, BaseRsp, BaseSchema


class ExampleData(BaseModel):
    field: str


class ExampleInResponse(BaseRsp):
    data: ExampleData


class ExampleCreate(BaseSchema):
    ...
