from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/english_schema"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """Creates a new database session and ensures proper cleanup."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
