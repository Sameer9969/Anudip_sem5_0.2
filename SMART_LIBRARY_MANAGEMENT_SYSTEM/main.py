# SMART LIBRARY MANAGEMENT SYSTEM
# Main File


from library_system import Library


# Library ka object
library = Library()


# Menu
while True:

    print("\n====================================")
    print("   SMART LIBRARY MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Sort Books")
    print("8. Show Available Books")
    print("9. Show Issued Books")
    print("10. Waiting List")
    print("11. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":

        library.add_book()


    elif choice == "2":

        library.display_books()


    elif choice == "3":

        library.search_book()


    elif choice == "4":

        library.issue_book()


    elif choice == "5":

        library.return_book()


    elif choice == "6":

        library.delete_book()


    elif choice == "7":

        library.sort_books()


    elif choice == "8":

        library.available_books()


    elif choice == "9":

        library.issued_books()


    elif choice == "10":

        library.show_waiting_list()


    elif choice == "11":

        print("Thank you for using Smart Library!")

        break


    else:

        print("Invalid choice!")