from sqlalchemy import Column, String, Integer

from core.database import Base


# Model for Test
class TestModel(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    desc = Column(String(255))
