from static_data import MSG
from lib_api import LibAPI
import storage as stor


def main():
    while True:
    
        print(MSG.info.STARTUP_MESSAGE)
        option = input("# ")
        
        match option:
            case "0":
                LibAPI.display_books()
            case "1":
                LibAPI.add_book()
            case "2":
                LibAPI.delete_book()
            case "3":
                LibAPI.search_book()
            case "4":
                LibAPI.change_status_book()
            case _:
                print("Unrecognized option")

if __name__ == '__main__':
    stor.create_empty_storage()
    
    while True:
        try:
            main()
        except KeyboardInterrupt:
            question = input("\nDo you want to exit? (Y/N) \n")
            if question.casefold() in ('y', 'yes', 'ye'):
                print('Goodbye ...')
                exit(0)

