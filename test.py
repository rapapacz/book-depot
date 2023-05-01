from Book import Book
from BookSerializer import BookSerializer

test_book = Book('Test Author', 'Genre', 'ISBN', 100, 'Test Publisher', 2023, 1, 'Test Title', 'Test Translator')
BookSerializer.serialize(test_book)