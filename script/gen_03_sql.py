import os
import csv


input_dir_path = "C:\\Users\\arthur\\Documents\\English_voc\\all\\all_word.csv"
output_sql_path = "C:\\Users\\arthur\\PycharmProjects\\english_voc\\data\\03_feed_table_voc.sql"


def read_csv_folder(dir_path):
    fr = []
    en = []
    if os.path.isfile(input_dir_path) and input_dir_path.endswith(".csv"):
        try:
            with open(input_dir_path, mode='r', encoding='utf-8') as fichier:
                lecteur_csv = csv.reader(fichier, delimiter=',')

                # Sauter la première ligne (en-tête)
                next(lecteur_csv)

                # Itération sur chaque ligne
                for ligne in lecteur_csv:
                    if len(ligne) >= 2:  # Vérifie que la ligne a au moins 2 colonnes
                        fr.append(ligne[0])  # Ajoute la 1ère colonne à la liste
                        en.append(ligne[1])  # Ajoute la 2ème colonne à la liste

        except FileNotFoundError:
            print(f"Le fichier '{input_dir_path}' n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    return fr, en


def genere_sql_file(french_words, english_words, sql_path):
    # Nombre de lignes par lot
    batch_size = 100

    # Nom du fichier de sortie

    # Écriture dans le fichier par lots
    with open(sql_path, "w", encoding="utf-8") as file:
        for i in range(0, len(french_words), batch_size):
            # Obtenir un lot de données
            batch_french = french_words[i:i + batch_size]
            batch_english = english_words[i:i + batch_size]

            # Générer le script SQL pour ce lot
            sql_script = "INSERT INTO english_schema.vocabulary (french_word, english_word) VALUES\n"
            values = []
            for french, english in zip(batch_french, batch_english):
                values.append(f"(\"{french}\", \"{english}\")")
            sql_script += ",\n".join(values) + ";\n\n"

            # Écrire le script SQL dans le fichier
            file.write(sql_script)


fr, en = read_csv_folder(input_dir_path)
genere_sql_file(fr, en, output_sql_path)
