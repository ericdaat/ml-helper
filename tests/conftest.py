import os
import logging

from src.init_db import init_db
from src.config import TEST_DATABASE_URL


os.environ["TEST_ENVIRONMENT"] = "True"
logging.basicConfig(format=logging.DEBUG)


def pytest_configure():
    init_db(TEST_DATABASE_URL)
