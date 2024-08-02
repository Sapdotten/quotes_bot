from sqlalchemy import Column, ForeignKey, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    __tableargs__ = {"comment": "Table with users of app"}

    id = Column(
        Integer, nullable=False, unique=True, primary_key=True, autoincrement=True
    )
    task = Column(Text, unique=False, nullable = True)
