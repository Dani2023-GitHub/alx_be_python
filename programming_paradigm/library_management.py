#library managemenet system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    
    def set_status(self, status):
        self.__is_checked_out = status

    def get_status(self):
        return self.__is_checked_out


class Library:
    def __init__(self):
        self.__book = []

    def add_book(self, book):
        self.__book.append(book)

    def check_out_book(self, title):
        for book in self.__book:
            if book.title == title:
                book.set_status(True)
    
    def return_book(self, title):
        for book in self.__book:
            if book.title == title:
                book.set_status(False)

    def list_available_books(self):
        for book in self.__book:
            if book.get_status() == False:
                print(book.title, book.author)       
