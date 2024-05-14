import sqlite3

def create_history_table():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                      id INTEGER PRIMARY KEY,
                      user_id INTEGER NOT NULL,
                      command TEXT NOT NULL,
                      arguments TEXT,
                      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                      )''')
    conn.commit()
    conn.close()

def insert_user_history(user_id, command, arguments):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (user_id, command, arguments) VALUES (?, ?, ?)",
                   (user_id, command, arguments))
    conn.commit()
    conn.close()

def get_user_history(user_id):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute("SELECT command, arguments FROM history WHERE user_id=? "
                   "ORDER BY id DESC LIMIT 10",
                   (user_id,))
    history = cursor.fetchall()
    conn.close()
    return history

def log_command(user_id, command, arguments=None):
    insert_user_history(user_id, command, arguments)
