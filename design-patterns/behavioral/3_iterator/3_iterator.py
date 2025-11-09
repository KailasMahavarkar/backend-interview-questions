from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class BookCollection:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def create_iterator(self):
        return BookIterator(self._books)

class BookIterator(Iterator):
    def __init__(self, books):
        self._books = books
        self._index = 0
    
    def has_next(self):
        return self._index < len(self._books)
    
    def next(self):
        if self.has_next():
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration

# Usage
collection = BookCollection()
collection.add_book("Design Patterns")
collection.add_book("Clean Code")

iterator = collection.create_iterator()
while iterator.has_next():
    print(iterator.next())