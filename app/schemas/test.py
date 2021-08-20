from pydantic import BaseModel, validator

from schemas.validators import normalize, len_validator_10_to_255, len_validator_4_to_20


# Schemas for Test
class TestCreate(BaseModel):
    name: str
    desc: str

    # Validators
    _normalize_name = validator("name")(normalize)
    _validate_name_len = validator("name")(len_validator_4_to_20)
    _validate_desc_len = validator("desc", allow_reuse=True)(len_validator_10_to_255)


class TestUpdate(BaseModel):
    desc: str

    # Validators
    _validate_desc_len = validator("desc", allow_reuse=True)(len_validator_10_to_255)


class Test(TestCreate):
    id: int

    class Config:
        orm_mode = True
