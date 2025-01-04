import os
import pandas as pd

input_dir_path = "C:\\Users\\arthur\\Documents\\English_voc"
output_csv_path = "C:\\Users\\arthur\\Documents\\English_voc\\all\\all_word.csv"

# Vérifie si le fichier de sortie existe déjà
file_exists = os.path.exists(output_csv_path)

# Ouvre le fichier de sortie en mode ajout
with open(output_csv_path, mode='a', newline='', encoding='utf-8') as file:
    # Si le fichier n'existe pas, écrire les en-têtes
    if not file_exists:
        file.write("french,english\n")

    # Parcourt tous les fichiers dans le dossier
    for filename in os.listdir(input_dir_path):
        if filename.endswith('.csv'):
            # Crée le chemin complet vers le fichier .csv
            file_path = os.path.join(input_dir_path, filename)

            try:
                df = pd.read_csv(file_path, sep=',', on_bad_lines='skip', header=None)
            except Exception as e:
                print(f"Erreur avec le fichier {filename} en utilisant ',' : {e}")
                df = None

            # Extrait les deux premières colonnes
            if df.shape[1] >= 2:  # Vérifie qu'il y a au moins deux colonnes
                french_english = df.iloc[:, :2]  # Sélectionne les deux premières colonnes

                # Ajoute les lignes du fichier au fichier de sortie
                french_english.to_csv(file, header=False, index=False)

print("Les données ont été ajoutées avec succès dans", output_csv_path)
