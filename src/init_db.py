import logging

from sqlalchemy_utils import create_database, database_exists

from src.config import DATABASE_URL
from src.model import metadata, engine


def init_db(database_url):
    if not database_exists(database_url):
        create_database(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)

    logging.info("DB initialized.")


if __name__ == "__main__":
    init_db(DATABASE_URL)
