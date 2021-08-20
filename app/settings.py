from os import environ
from pydantic import BaseSettings


ENVIRON_APP_PREFIX = "fastapi_".upper()

DEFAULT_VALUES = {
    "APP_NAME": "My APP",
    "DATABASE_URI":  "sqlite:///./app.db"
}


def get_env_variables() -> dict:
    return {
        key.replace(ENVIRON_APP_PREFIX, ""): value
        for key, value in environ.items()
        if key.startswith(ENVIRON_APP_PREFIX)
        and key.replace(ENVIRON_APP_PREFIX, "") in DEFAULT_VALUES.keys()
    }


def load_settings() -> dict:
    return {**DEFAULT_VALUES, **get_env_variables()}


APP_SETTINGS = load_settings()


class Settings(BaseSettings):
    app_name: str = APP_SETTINGS.get("APP_NAME")
    database_uri: str = APP_SETTINGS.get("DATABASE_URI")
