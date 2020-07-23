from sqlalchemy import Column, Integer, JSON, String
from sqlalchemy.orm import relationship

from database import Base


class Games(Base):
    __tablename__ = "games_info"

    id = Column(Integer, primary_key=True, index=True)
    game_info = Column(JSON)
    hash_game = Column(String)