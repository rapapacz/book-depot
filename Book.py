from dataclasses import dataclass

@dataclass
class Book:
    def __init__ (self, author, genre, isbn, pages, publisher, publication_year, status, title, translator):
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.pages = pages
        self.publisher = publisher
        self.publication_year = publication_year
        self.status = status
        self.title = title
        self.translator = translator

