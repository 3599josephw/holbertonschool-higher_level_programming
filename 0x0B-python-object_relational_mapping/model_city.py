#!/usr/bin/python3
"""task 14 - City Class"""

from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """City Class inherting from Base, child to State"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
