#library managemenet system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    
    def return_book(self):
        self.__is_checked_out = False

    def check_out_book(self):
        self.__is_checked_out = True

    def get_status(self):
        return self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                book.check_out_book()
    
    def return_book(self,title):
        for book in self.__books:
            if book.title == title:
                book.return_book()

    def list_available_books(self):
        for book in self.__books:
            if book.get_status() == False:
                print(book.title, book.author)       
