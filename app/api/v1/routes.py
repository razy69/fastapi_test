from fastapi import APIRouter

from api.v1.test import test_router

# Api V1 routes declaration
api_router = APIRouter()
api_router.include_router(test_router)
