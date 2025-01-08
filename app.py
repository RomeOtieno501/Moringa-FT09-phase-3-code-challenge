from database.setup import create_tables
from models.author import Author
from models.article import Article
from models.magazine import Magazine

def main():
    # Initialize database
    create_tables()

    # Get user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create objects and save to database
    author = Author(author_name)
    author.save_to_db()

    magazine = Magazine(magazine_name, magazine_category)
    magazine.save_to_db()

    article = Article(article_title, article_content, author.id, magazine.id)
    article.save_to_db()

    # Display created records
    print("\nCreated Records:")
    print(author)
    print(magazine)
    print(article)

if __name__ == "__main__":
    main()
