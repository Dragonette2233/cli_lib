from abc import ABC

class BookModel(ABC):
    def __init__(self) -> None:
        
        self.id: int
        self.status: str
        self.title: str
        self.author: str
        self.year: int
        
    def set_title(self):
        ...
        
    def set_author(self):
        ...
    
    def set_year(self):
        ...
    
    def to_dict(self) -> dict:
        ...