import tkinter
import pymysql
import PIL
from AddBook import *


my_database = '' # The database name
my_password = 'Gorth$1999' # use your own password

my_connection = pymysql.connect(host="localhost", user="root", password=my_password, database=my_database) # root is the username here
my_cursor = my_connection.cursor() # cursor -> cursor

class Book:
    def __init__(self, id_book, name_book, author, publisher, types, quantity, storage, borrowed=True, content=''):
        super().__init__()
        self.id_book = id_book
        self.name_book = name_book
        self.author = author
        self.publisher = publisher
        self.types = types
        self.quantity = quantity
        self.content = content
        self.storage = storage
        self.borrowed = borrowed

    def AddBook(self):
        pass

    def DeleteBook(self):
        pass

    def ViewBook(self):
        pass


class BorrowedBook(Book):
    def __init__(self, id_person, id_librarian, id_book, borrowed_date, returned_date, returned=False, notes=''):
        super().__init__()
        self.id_person = id_person
        self.id_librarian = id_librarian
        self.id_book = id_book
        self.borrowed_date = borrowed_date
        self.returned_date = returned_date
        self.returned = returned
        # self.notes = notes


class Borrower:
    def __init__(self, id_person, full_name, gender, birth_day, address, can_borrow=None, origin=None):
        super().__init__()
        self.id_person = id_person
        self.full_name = full_name
        self.gender = gender
        self.birth_day = birth_day
        self.address = address
        self.can_borrow = can_borrow
        self.origin = origin

    def AddPerson(self):
        pass

    def DeletePerson(self):
        pass

    def FixPerson(self):
        pass

class Librarian:
    def __init__(self, id_librarian, full_name, gender, birth_day, address):
        super().__init__()
        self.id_librarian = id_librarian
        self.full_name = full_name
        self.gender = gender
        self.birth_day = birth_day
        self.address = address


# class Reports:
#     def __init__(self, date_add, sum_add_book, ):
#         super().__init__()

class RegistrationForm:
    def __init__(self, id_person, full_name, gender):
        super().__init__()
        self.id_card = id_person
        self.full_name = full_name
        self.gender = gender

class BorrowedForm:
    def __init__(self, id_person, id_librarian, id_book, borrowed_date):
        super().__init__()
        self.id_card = id_person
        self.id_librarian = id_librarian
        self.id_book = id_book
        self.borrowed_date = borrowed_date

class ReturnedForm:
    def __init__(self, id_person, id_librarian, id_book, borrowed_date, returned_date):
        super().__init__()
        self.id_card = id_person
        self.id_librarian = id_librarian
        self.id_book = id_book
        self.borrowed_date = borrowed_date
        self.returned_date = returned_date














