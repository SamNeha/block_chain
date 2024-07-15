class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = {"author": author, "available": True}

    def is_book_available(self, title):
        return title in self.books and self.books[title]["available"]

    def mark_book_as_unavailable(self, title):
        if title in self.books:
            self.books[title]["available"] = False

    def mark_book_as_available(self, title):
        if title in self.books:
            self.books[title]["available"] = True

    def print_inventory(self):
        print("Current Book Inventory:")
        for title, details in self.books.items():
            status = "Available" if details["available"] else "Not Available"
            print(f"{title} by {details['author']}: {status}")
