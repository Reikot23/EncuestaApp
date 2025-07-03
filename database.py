import sqlite3

conn = sqlite3.connect ('encuesta.db')

c = conn.cursor()

c.execute ('''

CREATE TABLE IF NOT EXISTS respuestas (
id INTEGER PRIMARY KEY AUTOINCREMENT,
          nombre TEXT NOT NULL,
          opinion TEXT NOT NULL
          )
''')

conn.commit()
conn.close()