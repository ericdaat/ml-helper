import os
import logging

os.environ["TEST_ENVIRONMENT"] = "1"

from src.init_db import init_db
from src.config import DATABASE_URL


logging.basicConfig(format=logging.DEBUG)


def pytest_configure():
    init_db(DATABASE_URL)
