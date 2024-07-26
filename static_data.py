import sys
from datetime import datetime

# sys.tracebacklimit = 0
CURRENT_YEAR = str(datetime.now().year)
BOOKS_STORAGE_FILE = 'books_db.json'

class InpMessage:
    DEL_BOOK = "Provide book ID which you want to remove from Lib: "
    CHANGE_STATUS_BOOK = "Provide book ID which you want to take: "
    ASK_FOR_EXIT = "\nDo you want to exit? (Y/N) \n"
    ASK_FOR_MATCHES = "Provide title, author or year for getting matches: "

class ErrMessage:
    YEAR_RELASE = "!! Book release year must be less than current %s year\n" % CURRENT_YEAR
    YEAR_INTEGER = "!! Book release year must be integer from 0 to current_year"
    TITLE_LENGTH = "!! Title length must be less than {char_limit} characters \n"
    AUTHOR_LENGTH = "!! Author length must be less than {char_limit} characters \n"
    EMPTY_FIELD = "!! Field cant be empty"

class InfoMessage:
    BOOK_REMOVED = 'Book removed from lib\n'
    BOOK_STATUS_CHANGED = 'Book status changed\n'
    BOOK_NOT_FOUND = "Book(s) not found"
    BOOK_ADDED = "Book addded succesfull"
    

    STARTUP_MESSAGE = """
    -- Welcome to CLI Library [for usage details - README.md] --
    
    Choose option
    0 - Display book DB
    1 - Add new book 
    2 - Delete book
    3 - Search for book (by ID)
    4 - Change book status \n\n
    """.replace('/\\t/', ' ')
    
class MSG:
    
    """
        Constant strings for stdout with prints and inputs
    
    """
    
    inp = InpMessage
    err = ErrMessage
    info = InfoMessage
