import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS birds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    avg_weight REAL     -- average weight as a number (float)
);
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS bird_descriptions (
    bird_id INTEGER PRIMARY KEY,
    description TEXT,
    FOREIGN KEY (bird_id) REFERENCES birds(id) ON DELETE CASCADE
);
''')

conn.commit()
conn.close()

print("Database and tables created successfully.")
