from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.api.base import api_router
from app.db.base import engine, Base


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

    # bind the database
    Base.metadata.create_all(bind=engine)

    # add logger
    # logger = logging.getLogger(logger_settings.LOGGER_NAME)

    # add the endpoints to the app
    app.include_router(api_router)

    # mount pictures
    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

    return app


app = get_application()
