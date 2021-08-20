#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI

from settings import Settings
SETTINGS = Settings()

from core.database import Base, engine
from api.v1.routes import api_router as v1


logger = uvicorn.logging.logging.getLogger()

# Create needed database tables
Base.metadata.create_all(bind=engine)

# Start app
app = FastAPI()
logger.error(SETTINGS.app_name)

# Add subrouters
app.include_router(v1, prefix="/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True)
