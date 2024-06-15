import sqlite3

def create_connection():
    conn = sqlite3.connect('mydatabase.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_record(name, age):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO records (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

def get_records():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM records')
    records = cursor.fetchall()
    conn.close()
    return records

def update_record(record_id, name, age):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE records SET name = ?, age = ? WHERE id = ?', (name, age, record_id))
    conn.commit()
    conn.close()

def delete_record(record_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM records WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()

# Initialize the database and table
create_table()
