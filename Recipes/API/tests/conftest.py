import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.main import app
from app.models import table_registry
from app.core.config import settings

@pytest.fixture(scope="module")
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
