from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging

from app.core.config import settings, logger_settings
from app.api.api import api_router


def get_application():
    # create the app
    app = FastAPI(title=settings.PROJECT_NAME)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # add logger
    logger = logging.getLogger(logger_settings.LOGGER_NAME)

    logger.info("dummy hi")

    # add the endpoints to the app
    app.include_router(api_router)

    return app


app = get_application()
