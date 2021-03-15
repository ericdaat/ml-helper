import logging

import pytest
from src.init_db import init_db

logging.basicConfig(format=logging.DEBUG)


@pytest.fixture
def db():
    init_db()

    yield db
