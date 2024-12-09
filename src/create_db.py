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
    tags TEXT DEFAULT NULL,
    type TEXT,
    inner_url TEXT,
    outer_url TEXT,
    final_url TEXT DEFAULT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    PROSSED BOOLEAN DEFAULT FALSE 
)
''')

# Sauvegarde et fermeture
conn.commit()
conn.close()

print("Table créée avec succès.")
