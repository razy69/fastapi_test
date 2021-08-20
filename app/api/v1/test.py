from fastapi_crudrouter import SQLAlchemyCRUDRouter

from schemas.test import Test, TestCreate, TestUpdate
from models.test import TestModel
from core.database import get_db


# Test crud router
test_router = SQLAlchemyCRUDRouter(
    schema=Test,
    create_schema=TestCreate,
    update_schema=TestUpdate,
    db_model=TestModel,
    db=get_db,
    prefix="test"
)
