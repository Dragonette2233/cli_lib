import datetime
from static_data import MSG

def data_received(func):
    def decorator(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                break
            except LibError as e:
                print(e)
        return result
    return decorator

class LibError(Exception): ...
class YearError(LibError): ...
class TitleError(LibError): ...
class AuthorError(LibError): ...
class EmptyError(LibError): ...
class SymbolsError(LibError): ...
    
class Validation:
    
    """
        Dinstinct class for validation and returning input based on input field    

    
    """
    
    @staticmethod
    def __empty(field, value):
        if len(value) < 1:
            raise EmptyError(MSG.err.EMPTY_FIELD)
        
    @staticmethod
    def year(value):
        
        try:
            value = int(value)
            
            if value <= 0:
                raise YearError(MSG.err.YEAR_INTEGER)
        except (TypeError, ValueError):
            raise YearError(MSG.err.YEAR_INTEGER)
        
        if int(value) > datetime.datetime.now().year:
            raise YearError(MSG.err.YEAR_RELASE)
        
        return value
    
    @staticmethod
    def title(value):
        Validation.__empty('title', value)
        
        if len(value) > 100:
            raise TitleError(MSG.err.TITLE_LENGTH.format(char_limit=100))

        return value
        
    
    @staticmethod
    def author(value):
        Validation.__empty('author', value)
        
        if len(value) > 70:
            raise AuthorError(MSG.err.AUTHOR_LENGTH.format(char_limit=70))
        
        return value
        