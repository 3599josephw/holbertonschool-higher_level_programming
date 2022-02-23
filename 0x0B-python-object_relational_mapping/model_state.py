#!/usr/bin/python3
"""task 6 - State Class"""

from sqlalchemy import Column, Integer, String, create_engine, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State model inheriting from Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
