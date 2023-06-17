from typing import Callable

from fastapi import FastAPI

from app.models.events import init_indexs


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        await init_indexs(app)

    return start_app
