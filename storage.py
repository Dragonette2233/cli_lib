import json
import os
from abstract import BookModel
from static_data import BOOKS_STORAGE_FILE

def create_empty_storage() -> None:
    # Проверяем, существует ли файл
    if not os.path.exists(BOOKS_STORAGE_FILE):
        # Создаем и записываем в него пустой список
        with open(BOOKS_STORAGE_FILE, 'w', encoding='utf-8') as file:
            json.dump([], file)

def update_lib(data: list[dict]):
    
    """
        Updating books_db.json with new essence
    
    """
    
    
    with open(BOOKS_STORAGE_FILE, mode='w+', encoding='utf-8') as book_db:
        json.dump(data, book_db, indent=4)

def get_books(id_=None) -> tuple[list[dict[str, str | int]], dict]:
    
    """

    
    returns ``tuple``:
        First value ``list[dict]`` - all books base 
        
        Second value ``dict``- single book by ``id_`` if provided, else empty dict
        
        
    """
    
    with open(BOOKS_STORAGE_FILE, mode='r', encoding='utf-8') as book_db:
        
        books_as_list = json.load(book_db)
        chosen_book = {}
        
        if id_:
            for b in books_as_list:
                if b['id'] == id_:
                    chosen_book = b
                    break

    return [books_as_list, chosen_book]

def put_new_book(book: BookModel = None) -> None:
    
    """
        Updating books library (books_db.json) with new ``book`` value
    
    """

    books_storage, _ = get_books()
    books_storage.append(book.to_dict())
    
    update_lib(books_storage)
                
def get_uniq_id() -> int:
    
    """
        Generates unique ID ( > 0 ) based on existig values in books_db.json
    
    """
    
    books_storage, _ = get_books()
        
    if len(books_storage) == 0:
        return 1
    
    return books_storage[-1]['id'] + 1