from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


# Configuration SQLAlchemy
Base = declarative_base()

# Définir le modèle pour la table `vocabulary`
class Vocabulary(Base):
    __tablename__ = 'vocabulary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    french_word = Column(String(255), nullable=False)
    english_word = Column(String(255), nullable=False)
    session_id = Column(Integer, nullable=True)

# Créer le moteur SQLAlchemy
def get_engine():
    engine = create_engine(
        "mysql+mysqlconnector://root:root@localhost/english_schema"
    )
    return engine


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


def add_word(french_word: str, english_word: str):
    session = get_session()
    new_word = Vocabulary(french_word=french_word, english_word=english_word)
    session.add(new_word)
    session.commit()
    session.close()


def del_french_word(french_word: str) -> int:
    session = get_session()
    deleted_rows = session.query(Vocabulary).filter(Vocabulary.french_word == french_word).delete()
    session.commit()
    session.close()
    return deleted_rows

def del_english_word(english_word: str) -> int:
    session = get_session()
    deleted_rows = session.query(Vocabulary).filter(Vocabulary.english_word == english_word).delete()
    session.commit()
    session.close()
    return deleted_rows


def get_random_word():
    session = get_session()
    word = session.query(Vocabulary).order_by(func.rand()).first()
    session.close()
    return word


def make_session():
    session = get_session()

    # Trouver le plus grand session_id existant
    max_session_id = session.query(func.max(Vocabulary.session_id)).scalar() or 0

    # Récupérer 20 mots sans session_id
    words_to_update = session.query(Vocabulary).filter(Vocabulary.session_id == None).limit(20).all()

    # Attribuer le nouvel id de session à ces mots
    new_session_id = max_session_id + 1
    for word in words_to_update:
        word.session_id = new_session_id

    # Sauvegarder les modifications
    session.commit()
    session.close()

    print(f"New session (ID : {new_session_id}) created with {len(words_to_update)} words.")


def reset_session(session_id=None):
    session = get_session()

    try:
        if session_id is None:
            # Mettre tous les session_id à None
            session.query(Vocabulary).update({Vocabulary.session_id: None})
        else:
            # Mettre à None uniquement les session_id qui correspondent à l'argument
            session.query(Vocabulary).filter(Vocabulary.session_id == session_id).update({Vocabulary.session_id: None})

        # Sauvegarder les modifications
        session.commit()

        print(f"Session IDs reset to None{' for session_id ' + str(session_id) if session_id is not None else ''}.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()


def reset_learning(session_id=None):
    session = get_session()

    try:
        if session_id is None:
            # Mettre tous les session_id à None
            session.query(Vocabulary).update({Vocabulary.learned: None})
        else:
            # Mettre à None uniquement les learned correspondant au session_id en argument
            session.query(Vocabulary).filter(Vocabulary.session_id == session_id).update({Vocabulary.learbed: None})

        # Sauvegarder les modifications
        session.commit()

        print(f"Learned reset to None{' for session_id ' + str(session_id) if session_id is not None else ''}.")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()


def get_words(session_id=None):
    session = get_session()

    try:
        if session_id is None:
            # Trouver le plus grand session_id existant
            session_id = session.query(func.max(Vocabulary.session_id)).scalar()
            if session_id is None:
                print("No sessions available to play.")
                return []

        # Récupérer les mots du session_id
        words = session.query(Vocabulary).filter(Vocabulary.session_id == session_id).all()

        if not words:
            print(f"No words found for session_id {session_id}.")
            return []
        else:
            return words


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


# Créer la table (si elle n'existe pas déjà)
if __name__ == "__main__":
    word = get_random_word()
    print(f"Word : {word.french_word} -> {word.english_word}")
