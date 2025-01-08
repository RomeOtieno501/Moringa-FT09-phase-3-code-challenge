from database.connection import get_db_connection

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    def articles(self):
        from models.article import Article  # Lazy import to avoid circular imports
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in rows]

    def magazines(self):
        from models.magazine import Magazine  # Lazy import to avoid circular imports
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT DISTINCT m.* 
                           FROM magazines m 
                           JOIN articles a ON m.id = a.magazine_id 
                           WHERE a.author_id = ?''', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(*row) for row in rows]

    def __repr__(self):
        return f"<Author {self.name}>"
