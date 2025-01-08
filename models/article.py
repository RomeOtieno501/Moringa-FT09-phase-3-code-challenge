from database.connection import get_db_connection

class Article:
    def __init__(self, title, content, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (self.title, self.content, self.author_id, self.magazine_id)
        )
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    def __repr__(self):
        return f"<Article {self.title}>"
