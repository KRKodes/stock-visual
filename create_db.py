import sqlite3

# Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('finance.db')
c = conn.cursor()

# Create a table to track API calls
c.execute('''
CREATE TABLE IF NOT EXISTS api_calls (
    id INTEGER PRIMARY KEY,
    count INTEGER NOT NULL
)
''')

# Initialize the count
c.execute('INSERT INTO api_calls (count) VALUES (0)')

# Save (commit) the changes and close the connection
conn.commit()
conn.close()
