import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('ai_tools.db')
cursor = conn.cursor()

# Création de la table
cursor.execute('''
CREATE TABLE ai_tools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    title TEXT,
    description TEXT,
    tags TEXT,
    link TEXT,
    type TEXT,
    final_url TEXT
)
''')

# Sauvegarde et fermeture
conn.commit()
conn.close()

print("Table créée avec succès.")
