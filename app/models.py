from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vocabulary(Base):
    """
    Represents the vocabulary table in the database.
    Each entry consists of a French word, its English translation,
    an optional session ID, and a flag indicating if the word has been learned.
    """
    __tablename__ = 'vocabulary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    french_word = Column(String(), nullable=False)
    english_word = Column(String(), nullable=False)
    session_id = Column(Integer, nullable=True)
    learned = Column(Boolean, nullable=True)
