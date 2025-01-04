from app.datamodel import (
    get_random_word,
    get_words,
    make_session,
    reset_learning,
    reset_session,
)

def quiz():
    print("Welcome to voc quizz !")
    print("Press help to list command and 'exit' to leave.\n")

    while True:

        user_input = input().strip()

        if user_input.lower() == "help":
            help()

        elif user_input.lower() == "new session":
            make_session()

        elif user_input.lower() == "reset session":
            main_reset_session()

        elif user_input.lower() == "random play":
            random_play()

        elif user_input.lower() == "play session":
            play_session()

        elif user_input.lower() == "reset learning":
            reset_learning()

        elif user_input.lower() == "exit":
            end()
            break

        else:
            print("Wrong command, please retry")


def help():
    print("Available command are :\nhelp\nnew session\nreset session\nrandom play\nplay session\nexit")


def main_reset_session():
    session_id = input("Enter the session_id to reset (or press Enter to reset all): ").strip()
    if session_id:
        try:
            session_id = int(session_id)
        except ValueError:
            print("Invalid session_id. Please enter a valid integer. Nothing is done")
        else:
            reset_session(session_id=session_id)
    else:
        reset_session()


def main_reset_learning():
    session_id = input("Enter the session_id to reset learned (or press Enter to reset all): ").strip()
    if session_id:
        try:
            session_id = int(session_id)
        except ValueError:
            print("Invalid session_id. Please enter a valid integer. Nothing is done")
        else:
            reset_learning(session_id=session_id)
    else:
        reset_learning()


def random_play():
    while True:
        print("Random play started\n Press 'stop' to stop.\n")

        # Obtenir un mot aléatoire
        word = get_random_word()
        if not word:
            print("Database is empty. Add word before play.")
            break

        print(f"Let's translate this : {word.french_word}")
        word_user_input = input("Your answer : ").strip()

        # Permet de quitter le quiz
        if word_user_input.lower() == "stop":
            print("Thanks for playing ! random play ended.")
            break

        # Vérification de la réponse
        if word_user_input.lower() == word.english_word.lower():
            print("Great ! 🎉\n")
        else:
            print(f"Fail. The correct answer was : {word.english_word}.\n")


def play_session():
    session_id = input("Enter the session_id to play (or press Enter to play last): ").strip()
    if session_id:
        try:
            session_id = int(session_id)
        except ValueError:
            print("Invalid session_id. Last session id used")
            session_id = None
    else:
        session_id = None

    words = get_words(session_id)

    print(f"Playing session with ID: {session_id} Press 'stop' to stop.\n")

    good_answer = 0
    bad_answer = 0
    for word in words:

        print(f"Let's translate this : {word.french_word}")
        word_user_input = input("Your answer : ").strip()

        # Permet de quitter le quiz
        if word_user_input.lower() == "stop":
            print("Thanks for playing! Session play ended.")
            break

        # Vérification de la réponse
        if word_user_input.lower() == word.english_word.lower():
            print("Great! 🎉\n")
            good_answer += 1
        else:
            print(f"Fail. The correct answer was : {word.english_word}.\n")
            bad_answer += 1

    print(f"Session ended with {good_answer}/{good_answer + bad_answer}")


def end():
    print("Thanks for playing ! Bye.")

if __name__ == "__main__":
    quiz()
