from sqlalchemy.orm import Session
from app.services import get_words_service, set_learned_status_service


def start_quiz(db: Session, session_id: int = None):
    """
    Start a quiz session. If no session ID is provided, the latest session is used.
    """
    session_id, words = get_words_service(db, session_id)

    if not words:
        print("No words available for this session.")
        return

    correct_answers = 0
    bad_answers = 0
    incorrect_words = []

    for word in words:
        answer = input(f"Translate '{word.french_word}' to English: ").strip().lower()

        if answer == word.english_word.lower():
            print("Correct!")
            set_learned_status_service(db, word.id, True)
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer was: {word.english_word}")
            set_learned_status_service(db, word.id, False)
            bad_answers += 1
            incorrect_words.append(word)

    print(f"====> Quiz completed! You got {correct_answers}/{len(words)} correct. Let's retry incorrecte word :\n")

    while incorrect_words:

        correct_answers = 0
        bad_answers = 0
        words_to_retry = []
        for word in incorrect_words:
            answer = input(f"Translate '{word.french_word}' to English: ").strip().lower()

            if answer == word.english_word.lower():
                print("Correct!")
                set_learned_status_service(db, word.id, True)
                correct_answers += 1
            else:
                print(f"Incorrect! The correct answer was: {word.english_word}")
                set_learned_status_service(db, word.id, False)
                bad_answers += 1
                words_to_retry.append(word)
        incorrect_words = words_to_retry

        if not incorrect_words:
            print(f"All words are now correct! You got {correct_answers}/{len(words)} correct.")
        else:
            print(f"Quiz completed for this round. You got {correct_answers}/{len(words)} correct.")
            print(f"You have {len(incorrect_words)} word(s) left to retry.")