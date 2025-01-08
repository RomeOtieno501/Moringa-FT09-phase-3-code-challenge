import sqlite3

def get_db_connection():
    """Establish and return a database connection."""
    return sqlite3.connect('magazine.db')
