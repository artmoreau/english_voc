from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.sql import cast
from sqlalchemy.types import String, Integer, Boolean
from app.models import Vocabulary


def add_word(db: Session, french_word: str, english_word: str):
    """Add a new word to the vocabulary table."""
    new_word = Vocabulary(french_word=french_word, english_word=english_word)
    db.add(new_word)
    db.commit()
    db.refresh(new_word)
    return new_word


def delete_word_by_french(db: Session, french_word: str) -> int:
    """Delete a word by its French version."""
    deleted_rows = db.query(Vocabulary).filter(cast(Vocabulary.french_word, String) == french_word).delete()
    db.commit()
    return deleted_rows


def delete_word_by_english(db: Session, english_word: str) -> int:
    """Delete a word by its English version."""
    deleted_rows = db.query(Vocabulary).filter(cast(Vocabulary.english_word, String) == english_word).delete()
    db.commit()
    return deleted_rows


def update_word(db: Session, french_word: str, new_english_translation: str) -> int:
    """Update the English translation of a given French word."""
    word_entry = db.query(Vocabulary).filter(cast(Vocabulary.french_word, String) == french_word).first()
    if word_entry:
        word_entry.english_word = new_english_translation
        db.commit()
        return 1
    return 0


def get_random_word(db: Session):
    """Retrieve a random word from the vocabulary table."""
    return db.query(Vocabulary).order_by(func.rand()).first()


def assign_session(db: Session):
    """Assign a new session ID to 20 words without a session."""
    max_session_id = db.query(func.max(Vocabulary.session_id)).scalar() or 0
    words_to_update = db.query(Vocabulary).filter(Vocabulary.session_id.is_(None)).limit(20).all()
    new_session_id = max_session_id + 1

    for word in words_to_update:
        word.session_id = new_session_id

    db.commit()
    return new_session_id, len(words_to_update)


def reset_session(db: Session, session_id: int = None):
    """Reset session IDs to None."""
    query = db.query(Vocabulary)
    if session_id:
        query = query.filter(cast(Vocabulary.session_id, Integer) == session_id)
    query.update({Vocabulary.session_id: None})
    db.commit()


def reset_learning(db: Session, session_id: int = None):
    """Reset the learned status of words in a given session."""
    query = db.query(Vocabulary)
    if session_id:
        query = query.filter(cast(Vocabulary.session_id, Integer) == session_id)
    query.update({Vocabulary.learned: None})
    db.commit()


def get_words(db: Session, session_id: int = None, learned: bool = None) -> tuple[int,list]:
    """Retrieve words based on session ID and learned status."""
    if session_id is None:
        session_id = db.query(func.max(Vocabulary.session_id)).scalar()
        if session_id is None:
            return 0, []

    query = db.query(Vocabulary).filter(cast(Vocabulary.session_id, Integer) == session_id)
    if learned is not None:
        query = query.filter(cast(Vocabulary.learned, Boolean) == learned)

    words = query.all()
    return session_id, words


def set_learned_status(db: Session, word_id: int, learned: bool):
    """Update the learned status of a specific word."""
    db.query(Vocabulary).filter(cast(Vocabulary.id, String) == word_id).update({Vocabulary.learned: learned})
    db.commit()
