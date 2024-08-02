import logging

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from database.database_settings import DBSettings


engine = create_async_engine(url=DBSettings.get_url(), echo=True)
logging.info("Engine for database is initialized")
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
logging.info("async_session is created")


@event.listens_for(engine.sync_engine, "connect")
def do_connect(dbapi_connection, connection_record):
    # disable aiosqlite's emitting of the BEGIN statement entirely.
    # also stops it from emitting COMMIT before any DDL.
    dbapi_connection.isolation_level = None

@event.listens_for(engine.sync_engine, "begin")
def do_begin(conn):
    # emit our own BEGIN
    conn.exec_driver_sql("BEGIN")