-- Sélection du schéma pour les prochaines opérations
USE english_schema;

-- Création de la table 'vocabulary'
CREATE TABLE IF NOT EXISTS vocabulary (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Identifiant unique
    english_word VARCHAR(255) NOT NULL,     -- Mot en anglais
    french_word VARCHAR(255) NOT NULL,      -- Traduction en français
    session_id INT NULL                     -- Session pour l'entrainement
    learned BOOLEAN NULL;                   -- Statut d'apprentissage
);