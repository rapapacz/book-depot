import json

class BookSerializer:

   @staticmethod
   def serialize(book_data):
       return json.dumps(book_data.__dict__)
