# English Vocabulary CLI

This is a command-line application for managing and quizzing vocabulary. The application allows you to add, delete, and manage words in a vocabulary list, as well as run quiz sessions. It interacts with a local SQL database to store the words and sessions. The SQL database is not included in the project, but SQL scripts are provided to generate the necessary tables.


## 📌 Installation

1. **Cloner le projet**  
   ```bash
   git clone https://github.com/artmoreau/english_voc.git
   cd english_voc
    ```

2. **install dependancies**
   ```bash
   pip install -r requirements.txt
    ```

3. **Setup the SQL vocabulary database locally**
   ```bash
    python sql_script/01_create_schema.py
    python sql_script/02_create_table_voc.py
    python sql_script/03_feed_table_voc.py
    ```

## 📂 Structure du Projet

- **english_voc/**
  - **app/**
    - `models.py` - Definition of SQLAlchemy models
    - `database.py` - Database connection and management
    - `crud.py` - Data manipulation functions (CRUD)
    - `services.py` - Quiz functionality
    - `quiz.py` - Allows importing app as a module
    - `__init__.py` - Permet d'importer `app` comme un module
  - **sql_script/**
    - `01_create_schema.py` - Creates the database schema
    - `02_create_table_voc.py` - Creates the vocabulary table
    - `03_feed_table_voc.py` - Fills the vocabulary table
  - `main.py` - Command-line interface for the quiz
  - `requirements.txt` - Project dependencies
  - `README.md` - Project documentation
  - `pyproject.toml` - Project management with Poetry


## 🎲 Commands


## `add-word`

Add a new word to the vocabulary.

```bash
python main.py add-word <french_word> <english_word>
```

- **Arguments**:
    - `french_word`: The word in French to add to the vocabulary.
    - `english_word`: The corresponding English translation of the French word.

---

## `delete-word`

Delete a word by its French version.

```bash
python main.py delete-word <french_word>
```

- **Arguments**:
    - `french_word`: The French word to delete from the vocabulary.

---

## `create-session`

Assign a new session ID to 20 words without one.

```bash
python main.py create-session
```

- **Arguments**: None

---

## `reset-session`

Reset session IDs to `None`.

```bash
python main.py reset-session [<session_id>]
```

- **Arguments**:
    - `session_id` (optional): The session ID to reset. If not provided, all session IDs will be reset.

---

## `start-session`

Start a quiz session of 20 word. If no session ID is provided, the latest session is used.

```bash
python main.py start-session [<session_id>]
```

- **Arguments**:
    - `session_id` (optional): The session ID to start. If not provided, the latest session will be used.

## 🚀 Projet développé par Arthur Moreau 🎯