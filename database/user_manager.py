import logging

from typing import Union

from database.models import User, Base
from sqlalchemy import text, select

from database.connect_db import engine, async_session


async def add_user(id: int, task: str) -> None:

    async with async_session() as session:
        user = await session.execute(select(User).where(User.id == id))
        user = user.scalars().first()
        if not user:
            new_user = User(id=id, task = task)
            session.add(new_user)
            await session.commit()
            logging.info(f"User {id} was added to db")
        else:
            user.task = task
            await session.commit()

async def get_task(id: int) -> Union[str, None]:
    async with async_session() as session:
        user = await session.execute(select(User).where(User.id == id))
        user = user.scalars().first()
        if not user:
            return None
        else:
            return user.task
        
async def change_task(id: int, task: str):
    async with async_session() as session:
        user = await session.execute(select(User).where(User.id == id))
        user = user.scalars().first()
        if not user:
            new_user = User(id=id, task = task)
            session.add(new_user)
            await session.commit()
            logging.info(f"User {id} was added to db")
        else:
            user.task = task
            await session.commit()
            
    
async def get_all_users():
    async with async_session() as session:
        tasks = await session.execute(select(User).where(True))
        tasks = tasks.scalars().all()
        if tasks:
            return [(i.id, i.task) for i in tasks]
        else:
            return []