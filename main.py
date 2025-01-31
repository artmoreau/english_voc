import click
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, quiz

@click.group()
def cli():
    """Command-line interface for managing vocabulary."""
    pass

@click.command()
@click.argument('french_word')
@click.argument('english_word')
def add_word(french_word, english_word):
    """
    Add a new word to the vocabulary.

    Arguments:
    french_word (str): The word in French that you want to add.
    english_word (str): The corresponding word in English.

    This command adds a new word pair (French -> English) to the vocabulary database.
    """
    db: Session = SessionLocal()
    crud.add_word(db, french_word, english_word)
    db.close()
    click.echo(f"Added word: {french_word} -> {english_word}")

@click.command()
@click.argument('french_word')
def delete_word(french_word):
    """
    Delete a word by its French version.

    Arguments:
    french_word (str): The French word to delete from the vocabulary.

    This command removes the given French word and its corresponding English word from the database.
    """
    db: Session = SessionLocal()
    deleted = crud.delete_word_by_french(db, french_word)
    db.close()
    if deleted:
        click.echo(f"Deleted word: {french_word}")
    else:
        click.echo(f"Word not found: {french_word}")

@click.command()
def create_session():
    """
    Assign a new session ID to words without one.

    Arguments: None

    This command assigns a new session ID to all words that currently don't have a session ID.
    It helps group words together for future quiz sessions.
    """
    db: Session = SessionLocal()
    session_id, count = crud.assign_session(db)
    db.close()
    click.echo(f"Started session {session_id} with {count} words.")

@click.command()
@click.argument('session_id', required=False, type=int)
def reset_session(session_id):
    """
    Reset session IDs to None.

    Arguments:
    session_id (int, optional): The session ID to reset. If not provided, all sessions are reset.

    This command removes the session ID from the specified session or all sessions, effectively clearing session associations.
    """
    db: Session = SessionLocal()
    crud.reset_session(db, session_id)
    db.close()
    click.echo("Session reset.")

@click.command()
@click.argument('session_id', required=False, type=int)
def start_session(session_id):
    """
    Start a quiz session. If no session ID is provided, the latest session is used.

    Arguments:
    session_id (int, optional): The session ID to start. If not provided, the latest session will be used.

    This command starts the quiz session by retrieving the words associated with the given session ID.
    If no session ID is provided, it will use the most recent session.
    """
    db: Session = SessionLocal()
    quiz.start_quiz(db, session_id)
    db.close()

# Adding all commands to the CLI
cli.add_command(add_word)
cli.add_command(delete_word)
cli.add_command(create_session)
cli.add_command(reset_session)
cli.add_command(start_session)

if __name__ == "__main__":
    cli()
