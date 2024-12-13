from app.datamodel import get_random_word

def quiz():
    print("Bienvenue au quiz de vocabulaire !")
    print("Tapez 'exit' pour quitter à tout moment.\n")

    while True:
        # Obtenir un mot aléatoire
        word = get_random_word()
        if not word:
            print("La base de données est vide. Ajoutez des mots avant de jouer.")
            break

        print(f"Traduisez ce mot en anglais : {word.french_word}")
        user_input = input("Votre réponse : ").strip()

        # Permet de quitter le quiz
        if user_input.lower() == "exit":
            print("Merci d'avoir joué ! À bientôt.")
            break

        # Vérification de la réponse
        if user_input.lower() == word.english_word.lower():
            print("Succès ! 🎉\n")
        else:
            print(f"Échec. La bonne réponse était : {word.english_word}.\n")

if __name__ == "__main__":
    quiz()
