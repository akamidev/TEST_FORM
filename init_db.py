# init_db.py
import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('data/form_data.db')
cursor = conn.cursor()

# Création de la table si elle n'existe pas déjà
cursor.execute('''
CREATE TABLE IF NOT EXISTS form_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

print("Table créée avec succès.")
conn.commit()
conn.close()
