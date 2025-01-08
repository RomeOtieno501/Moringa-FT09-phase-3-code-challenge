import unittest
from models.article import Article
from models.author import Author
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe")  # Pass only the name; ID will be None by default
        self.assertEqual(author.name, "John Doe")
        self.assertIsNone(author.id)  # ID should be None until saved to the database

    def test_article_creation(self):
        article = Article("Test Title", "Test Content", 1, 1)  # Correct initialization
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)
        self.assertIsNone(article.id)  # ID should be None until saved to the database

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")  # Correct initialization
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertIsNone(magazine.id)  # ID should be None until saved to the database

if __name__ == "__main__":
    unittest.main()
