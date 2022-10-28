
from multiprocessing.util import LOGGER_NAME
from typing import List, Union

from pydantic import AnyHttpUrl, BaseModel, BaseSettings, validator



class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DB_URL: str
    TEMPLATES_DIR: str
    STATIC_DIR: str
    TARGET_URL: str

    AMBASSADORS_TABLE: str = "ambassadors"
    VISITORS_TABLE: str = "visitors"


    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

class Logger(BaseSettings):
    LOGGER_NAME: str 
    LOG_FORMAT: str
    LOG_LEVEL: str

     # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "LOG_FORMAT",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "LOGGER_NAME": {"handlers": ["default"], "level": "LOG_LEVEL"},
    }

    class Config:
        case_sensitive = True
        env_file = ".env"

logger_settings = Logger()