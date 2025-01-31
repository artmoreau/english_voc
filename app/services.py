from sqlalchemy.orm import Session
from app import crud

def add_word_service(db: Session, french_word: str, english_word: str):
    """Service to add a new word."""
    return crud.add_word(db, french_word, english_word)

def delete_word_by_french_service(db: Session, french_word: str) -> int:
    """Service to delete a word by its French version."""
    return crud.delete_word_by_french(db, french_word)

def delete_word_by_english_service(db: Session, english_word: str) -> int:
    """Service to delete a word by its English version."""
    return crud.delete_word_by_english(db, english_word)

def update_word_service(db: Session, french_word: str, new_english_translation: str) -> int:
    """Service to update the English translation of a given French word."""
    return crud.update_word(db, french_word, new_english_translation)

def get_random_word_service(db: Session):
    """Service to retrieve a random word."""
    return crud.get_random_word(db)

def assign_session_service(db: Session):
    """Service to assign a new session ID to 20 words without a session."""
    return crud.assign_session(db)

def reset_session_service(db: Session, session_id: int = None):
    """Service to reset session IDs to None."""
    return crud.reset_session(db, session_id)

def reset_learning_service(db: Session, session_id: int = None):
    """Service to reset the learned status of words in a given session."""
    return crud.reset_learning(db, session_id)

def get_words_service(db: Session, session_id: int = None, learned: bool = None):
    """Service to retrieve words based on session ID and learned status."""
    return crud.get_words(db, session_id, learned)

def set_learned_status_service(db: Session, word_id: int, learned: bool):
    """Service to update the learned status of a specific word."""
    return crud.set_learned_status(db, word_id, learned)
