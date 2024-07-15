from blockchain import LibraryBlockchain
from library import Library
from user import User

def main():
    blockchain = LibraryBlockchain()
    library = Library()
    user_manager = User()

    # Adding books to the library
    library.add_book("1984", "George Orwell")
    library.add_book("Brave New World", "Aldous Huxley")

    # Registering users
    user_manager.register_user("User_1")
    user_manager.register_user("User_2")

    # Lending books
    if library.is_book_available("1984"):
        library.mark_book_as_unavailable("1984")
        user_manager.borrow_book("User_1", "1984")
        blockchain.add_transaction(f"Lent Book: '1984' to User_1")

    # Attempting to lend again
    if library.is_book_available("1984"):
        library.mark_book_as_unavailable("1984")
        user_manager.borrow_book("User_2", "1984")
        blockchain.add_transaction(f"Lent Book: '1984' to User_2")
    else:
        print("Book '1984' is not available.")

    # Returning books
    user_manager.return_book("User_1", "1984")
    library.mark_book_as_available("1984")
    blockchain.add_transaction(f"Returned Book: '1984' from User_1")

    # Print inventory and blockchain
    library.print_inventory()
    blockchain.print_chain()

if __name__ == '__main__':
    main()
