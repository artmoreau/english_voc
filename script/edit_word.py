from app.datamodel import edit_word

french_word = "le poisson "
english_word = "fish"

if edit_word(french_word, english_word):
    print("word edited")
else:
    print("mot non trouvé")
