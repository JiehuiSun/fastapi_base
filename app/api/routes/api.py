from fastapi import APIRouter

from . import example

router = APIRouter()
router.include_router(example.router, tags=["example"], prefix="/example")
