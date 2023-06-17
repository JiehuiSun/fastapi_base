# -*- coding: utf-8 -*-

from bson import ObjectId
from pydantic import BaseModel as PDBaseModel
from pydantic import Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class BaseModel(PDBaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
