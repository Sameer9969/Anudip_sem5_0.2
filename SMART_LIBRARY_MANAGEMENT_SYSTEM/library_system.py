# SMART LIBRARY MANAGEMENT SYSTEM
# Code File

from collections import deque


# -----------------------------
# Node for Linked List
# -----------------------------

class Node:

    def __init__(self, book):
        self.book = book
        self.next = None


# -----------------------------
# Library Class
# -----------------------------

class Library:

    def __init__(self):

        # Dictionary / Hashing
        # Book ID -> Book details
        self.books = {}

        # Linked List
        self.head = None

        # Queue for Waiting List
        self.waiting_list = deque()


    # -----------------------------
    # 1. Add Book
    # -----------------------------

    def add_book(self):

        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        # Check duplicate ID
        if book_id in self.books:
            print("Book already exists!")
            return

        # Book information
        book = {
            "id": book_id,
            "name": name,
            "author": author,
            "issued": False
        }

        # Store in Dictionary
        self.books[book_id] = book

        # Add book to Linked List
        new_node = Node(book)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        print("Book added successfully!")


    # -----------------------------
    # 2. Display Books
    # -----------------------------

    def display_books(self):

        if self.head is None:
            print("No books in library!")
            return

        print("\n===== ALL BOOKS =====")

        current = self.head

        while current is not None:

            book = current.book

            print(
                "ID:", book["id"],
                "| Name:", book["name"],
                "| Author:", book["author"],
                "| Issued:", book["issued"]
            )

            current = current.next


    # -----------------------------
    # 3. Search Book
    # -----------------------------

    def search_book(self):

        print("\n1. Search by ID")
        print("2. Search by Name")

        choice = input("Enter choice: ")

        # Search by ID
        if choice == "1":

            book_id = input("Enter Book ID: ")

            if book_id in self.books:

                book = self.books[book_id]

                print("\nBook Found!")
                print("ID:", book["id"])
                print("Name:", book["name"])
                print("Author:", book["author"])

            else:
                print("Book not found!")


        # Search by Name
        elif choice == "2":

            name = input("Enter Book Name: ")

            found = False

            # Linear Search
            for book in self.books.values():

                if book["name"].lower() == name.lower():

                    print("\nBook Found!")
                    print("ID:", book["id"])
                    print("Name:", book["name"])
                    print("Author:", book["author"])

                    found = True

            if found == False:
                print("Book not found!")

        else:
            print("Invalid choice!")


    # -----------------------------
    # 4. Issue Book
    # -----------------------------

    def issue_book(self):

        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        if book["issued"] == True:

            print("Book is already issued.")

            # Add student/person to waiting list
            name = input("Enter your name for waiting list: ")

            self.waiting_list.append(name)

            print("You have been added to waiting list.")

        else:

            book["issued"] = True

            print("Book issued successfully!")


    # -----------------------------
    # 5. Return Book
    # -----------------------------

    def return_book(self):

        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        if book["issued"] == False:

            print("This book was not issued.")

        else:

            book["issued"] = False

            print("Book returned successfully!")

            # Check waiting list
            if len(self.waiting_list) > 0:

                name = self.waiting_list.popleft()

                print(
                    "Waiting list:",
                    name,
                    "can now get the book."
                )


    # -----------------------------
    # 6. Delete Book
    # -----------------------------

    def delete_book(self):

        book_id = input("Enter Book ID: ")

        if book_id not in self.books:

            print("Book not found!")
            return

        # Delete from Dictionary
        del self.books[book_id]

        # Delete from Linked List
        current = self.head
        previous = None

        while current is not None:

            if current.book["id"] == book_id:

                if previous is None:

                    self.head = current.next

                else:

                    previous.next = current.next

                break

            previous = current
            current = current.next

        print("Book deleted successfully!")


    # -----------------------------
    # 7. Sort Books
    # -----------------------------

    def sort_books(self):

        if len(self.books) == 0:

            print("No books available!")
            return

        # Convert dictionary values into list
        book_list = list(self.books.values())

        # Sorting by Book Name
        book_list.sort(key=lambda x: x["name"].lower())

        print("\n===== BOOKS SORTED BY NAME =====")

        for book in book_list:

            print(
                "ID:", book["id"],
                "| Name:", book["name"],
                "| Author:", book["author"]
            )


    # -----------------------------
    # 8. Show Available Books
    # -----------------------------

    def available_books(self):

        print("\n===== AVAILABLE BOOKS =====")

        found = False

        for book in self.books.values():

            if book["issued"] == False:

                print(
                    "ID:", book["id"],
                    "| Name:", book["name"],
                    "| Author:", book["author"]
                )

                found = True

        if found == False:
            print("No available books!")


    # -----------------------------
    # 9. Show Issued Books
    # -----------------------------

    def issued_books(self):

        print("\n===== ISSUED BOOKS =====")

        found = False

        for book in self.books.values():

            if book["issued"] == True:

                print(
                    "ID:", book["id"],
                    "| Name:", book["name"],
                    "| Author:", book["author"]
                )

                found = True

        if found == False:
            print("No books are issued!")


    # -----------------------------
    # 10. Waiting List
    # -----------------------------

    def show_waiting_list(self):

        print("\n===== WAITING LIST =====")

        if len(self.waiting_list) == 0:

            print("Waiting list is empty!")

        else:

            position = 1

            for name in self.waiting_list:

                print(position, ".", name)

                position += 1