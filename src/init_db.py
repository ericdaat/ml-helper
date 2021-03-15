import logging

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from src.config import DATABASE_URL
from src.model import metadata

engine = db.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def init_db():
    if not database_exists(DATABASE_URL):
        create_database(DATABASE_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)

    logging.info("DB initialized.")


if __name__ == "__main__":
    init_db()
