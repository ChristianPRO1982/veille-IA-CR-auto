import sqlite3

conn = sqlite3.connect('ai_tools.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE ai_tools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    title TEXT,
    description TEXT,
    type TEXT,
    inner_url TEXT,
    outer_url TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE ai_tools_concat (
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
    prossed BOOLEAN DEFAULT FALSE 
)
''')

conn.commit()
conn.close()

print("Table créée avec succès.")