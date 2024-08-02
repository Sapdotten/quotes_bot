import logging

from sqlalchemy import text

from database.models import Base, User
from database.connect_db import engine

TABLES = [User,]


async def init_models():
    async with engine.begin() as conn:
        tables_exists = True
        try:
            await conn.run_sync(Base.metadata.create_all)
        except Exception:
            logging.info("Db already exists")
        else:
            logging.info("Creating db...")
            print("IS WORKING!")