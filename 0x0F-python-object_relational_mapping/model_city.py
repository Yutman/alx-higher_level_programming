#!/usr/bin/python3
"""Define a City class."""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """A class that defines a City instance."""

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
