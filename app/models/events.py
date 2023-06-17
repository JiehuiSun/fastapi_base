import importlib
import os

from fastapi import FastAPI

from app.core import logger


async def init_indexs(app: FastAPI) -> None:
    logger.info("Init index start..")
    models_pack_path: str = "app/models/domain"
    os.chdir(models_pack_path)

    for module in os.listdir("."):
        if module.endswith(".py") and module != "__init__.py":
            mo = importlib.import_module(
                f'{models_pack_path.replace("/", ".")}.{module.replace(".py", "")}'
            )
            models = []
            for model in dir(mo):
                if isinstance(getattr(mo, model), type) and getattr(
                    getattr(mo, model), "__coll__", None
                ):
                    models.append(getattr(mo, model))

            for model in models:
                if init_idx := getattr(model, "init_index", None):
                    await init_idx()

    logger.info("Init index success..")
