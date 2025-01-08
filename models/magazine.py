from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    def articles(self):
        from models.article import Article  # Lazy import to avoid circular imports
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in rows]

    def contributors(self):
        from models.author import Author  # Lazy import to avoid circular imports
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT DISTINCT a.* 
                           FROM authors a 
                           JOIN articles ar ON a.id = ar.author_id 
                           WHERE ar.magazine_id = ?''', (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(*row) for row in rows]

    def __repr__(self):
        return f"<Magazine {self.name}>"
