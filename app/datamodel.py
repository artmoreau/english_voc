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

# Créer la table (si elle n'existe pas déjà)
if __name__ == "__main__":
    word = get_random_word()
    print(f"Mot : {word.french_word} -> {word.english_word}")
