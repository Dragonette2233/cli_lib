import storage as stor
from static_data import MSG
from abstract import BookModel
from lib_utils import data_received, Validation


class Book(BookModel):
    def __init__(self) -> None:
        
        self.id = stor.get_uniq_id()
        self.status: str = 'Avaliable'
        self.title: str = ''
        self.author: str = ''
        self.year: int = 0
            
    @data_received
    def set_title(self):
        inp = input("# Title: ")
        self.title = Validation.title(inp)
        
    @data_received
    def set_author(self):
        inp = input("# Author: ")
        self.author = Validation.author(inp)
    
    @data_received
    def set_year(self):
        inp = input("# Year: ")
        self.year = Validation.year(inp)
    
    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'title': self.title,
            'author': self.author,
            'year': self.year
        }

class LibAPI:
    
    """
        Distinct API which provide functions with no arguments and no return values
    
    """
    
    @staticmethod
    def __fmt_book_display(books: list[dict], title: str) -> None:
        """
        Inner functions for printing formatted values
        
        Args:
            books (list[dict]): Body of message
            title (str): Head of message
        """
        
        
        books_as_list = [' - '.join(str(v) for v in b.values()) for b in books]
        
        print(title)
        print('ID - Status - Title - Author - Year\n')
        for b in books_as_list:
            print(b)
        
    
    
    @staticmethod
    def display_books() -> None:
        """
            Displaying all books from books_db.json
        
        """
        
        books, _ = stor.get_books()
        LibAPI.__fmt_book_display(books, '-- Books base --')
                
    @staticmethod
    def add_book() -> None:
        
        """
            Adding new book to books_db.json with input validations
            
        """
        
        book = Book()
        book.set_title()
        book.set_author()
        book.set_year()
        
        stor.put_new_book(book=book)
        print(MSG.info.BOOK_ADDED)

    @staticmethod
    def search_book() -> None:
        
        """
            Searching books by keywords, with checks in title, author and year, and displaying

        
        """
        
        kw = input(MSG.inp.ASK_FOR_MATCHES).strip().casefold()
        books, _ = stor.get_books()
        matches_by_kw = []
        
        for b in books:
            matches = [
                kw in b["title"].casefold(),
                kw in b["author"].casefold(),
                kw in b["status"].casefold(),
                kw == str(b["year"])
            ]
            
            if any(matches):
                matches_by_kw.append(b)
        
        if len(matches_by_kw) == 0:
            print(MSG.info.BOOK_NOT_FOUND)
        else:
            LibAPI.__fmt_book_display(matches_by_kw, title=f"-- Matches by keyword: {kw}")
                        
    @staticmethod
    def delete_book() -> None:
        """
            Removing book from library by ID
        
        """
        
        book_id = int(input(MSG.inp.DEL_BOOK))
        books, single_book = stor.get_books(id_=book_id)
    
        if single_book.get('id') == book_id:            
            books.remove(single_book)
            stor.update_lib(books)
            print(MSG.info.BOOK_REMOVED)
            
        else:
            print(MSG.info.BOOK_NOT_FOUND)
        
    @staticmethod
    def change_status_book() -> None:
        """
            Changing books status from Avaliable to Unavaliable
        
        """
        
        
        book_id = int(input(MSG.inp.CHANGE_STATUS_BOOK))
        books, single_book = stor.get_books()

        if single_book.get('id') == book_id:
            single_book['status'] = 'Unavaliable'
            print(MSG.info.BOOK_STATUS_CHANGED)
            stor.update_lib(books)
        else:
            print(MSG.info.BOOK_NOT_FOUND)