# SMART LIBRARY MANAGEMENT SYSTEM

A Python-based menu-driven library management project using core Data Structures and Algorithms (DSA) concepts such as dictionary/hash map, linked list, queue, searching, and sorting.

## Features
1. Add Book
2. Display Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Sort Books
8. Show Available Books
9. Show Issued Books
10. Waiting List

## DSA Concepts Used
- Dictionary / Hashing: Used to store books by unique book ID in a dictionary for fast lookup.
- Linked List: Used to store the list of books in a dynamic linked structure.
- Queue: Used for the waiting list when a book is unavailable and a user requests it.
- Searching: Linear search is used to locate a book by ID or title.
- Sorting: Books can be sorted by ID, title or author.

## How to Run
1. Open a terminal in the project folder.
2. Run the following command:

```bash
python smart_library_management.py
```

## Algorithm Explanation
### 1. Add Book
- Accept the book details from the user.
- Check whether the ID already exists in the dictionary.
- If it does not exist, create a Book object and store it in the hash map.
- Append the record to the linked list.

### 2. Display Books
- Traverse the linked list from the start to the end.
- Print each book's ID, title, author, quantity and available count.

### 3. Search Book
- Read the search keyword.
- Traverse all books in the linked list.
- Compare the search term with the book ID and title.
- If a match is found, print the record.

### 4. Issue Book
- Check whether the requested book exists.
- If the available quantity is greater than zero, issue the book and reduce availability.
- If no copy is available, add the request to the queue.

### 5. Return Book
- Search for the book by ID.
- Remove the borrower from the issued list.
- Increase the available count.
- After return, process the waiting queue if a request is waiting.

### 6. Delete Book
- Remove the book from the dictionary.
- Delete the node from the linked list.

### 7. Sort Books
- Collect all books from the linked list.
- Sort by the selected key: ID, title or author.
- Print the sorted list.

### 8. Show Available Books
- Traverse the linked list.
- Display only books whose available quantity is greater than zero.

### 9. Show Issued Books
- Traverse the linked list.
- Display books with at least one borrower.

### 10. Waiting List
- Use a queue to manage pending requests.
- Each waiting request is processed in First In, First Out (FIFO) order.

## Time Complexity
| Operation | Time Complexity |
|---|---|
| Add Book | O(1) average for dictionary insertion + O(n) linked list append |
| Display Books | O(n) |
| Search Book | O(n) |
| Issue Book | O(1) average for dictionary access |
| Return Book | O(1) average for list removal |
| Delete Book | O(n) (linked list traversal) |
| Sort Books | O(n log n) |
| Show Available Books | O(n) |
| Show Issued Books | O(n) |
| Waiting List | O(1) enqueue/dequeue |

## Sample Output
```text
========================================
SMART LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Display Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Sort Books
8. Show Available Books
9. Show Issued Books
10. Waiting List
0. Exit
========================================
```

## Notes
This project is designed as a mini project for academic learning and demonstrates how basic DSA structures can be used to build a real-world application.
