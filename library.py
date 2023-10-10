"""
  CS1026a 2023
  Assignment 02 Project 01
  Rohin Arya
  251371185
  rarya4
  Oct 10, 2023
"""

allBooks = [
    ["9780596007126", "The Earth Inside Out", "Mike B", 2, ["Ali"]],
    ["9780134494166", "The Human Body", "Dave R", 1, []],
    ["9780321125217", "Human on Earth", "Jordan P", 1, ["David", "b1", "user123"]],
]

rentedISBNs = []


def printMenu():
    print("\n######################")
    print("1: (A)dd a new book.")
    print("2: Bo(r)row books.")
    print("3: Re(t)urn a book.")
    print("4: (L)ist all books.")
    print("5: E(x)it.")
    print("######################\n")


def isValidISBN(isbn):
    if len(isbn) != 13:
        return False
    if not isbn.isnumeric():
        return False
    checksum = 0
    for i in range(0, len(isbn)):
        if i % 2 == 1:
            checksum += int(isbn[i]) * 3
        else:
            checksum += int(isbn[i])

    if checksum % 10 == 0:
        return True
    return False


def printBooks():
    for book in allBooks:
        print("---------------")
        if book[0] in rentedISBNs:
            print("[Unavailable]")
        else:
            print("[Available]")
        print(book[1] + " - " + book[2])
        print("E: " + str(book[3]) + " ISBN: " + book[0])
        print("Borrowed by: " + str(book[4]))


def start():
    while True:
        printMenu()
        choice = input("Enter your choice: ")
        print("Your choice is: " + choice)
        if choice == "1" or choice == "A" or choice == "a":
            book_name = input("Book name: ")
            while True:
                if "*" in book_name or "%" in book_name:
                    print("Invalid input. Please try again.")
                    book_name = input("Book name: ")
                else:
                    break
            book_author = input("Author name: ")
            book_edition = input("Edition: ")
            while True:
                if book_edition.isnumeric():
                    break
                else:
                    print("Invalid input. Please try again.")
                    book_edition = input("Edition: ")
            book_isbn = input("ISBN: ")
            if isValidISBN(book_isbn):
                # Check if already exists.
                for book in allBooks:
                    if book[0] == book_isbn:
                        print("Book already exists.")
                        break
                else:  # Triggered if for loop doesnt break.
                    allBooks.append(
                        [book_isbn, book_name, book_author, book_edition, []]
                    )
                    print("Book added successfully.")
            else:
                print("Invalid ISBN. Returning to menu.")
        elif choice == "2" or choice == "R" or choice == "r":
            borrower = input("Enter your name: ")
            search_term = input("Enter search term: ").lower()

            if search_term[len(search_term) - 1] == "*":
                # Contains mode
                search_term = search_term[:-1]
                foundBooks = []

                for book in allBooks:
                    if search_term in book[1].lower():
                        foundBooks.append(book)

            elif search_term[len(search_term) - 1] == "%":
                # Starts with mode
                search_term = search_term[:-1]
                foundBooks = []

                for book in allBooks:
                    if book[1].lower().startswith(search_term):
                        foundBooks.append(book)
            else:
                # Exact match mode
                foundBooks = []
                for book in allBooks:
                    if search_term == book[1].lower():
                        foundBooks.append(book)

            # Filter out books that are already rented.
            for book in foundBooks:
                if book[0] in rentedISBNs:
                    foundBooks.remove(book)

            # Borrow all foundBooks

            if len(foundBooks):
                print("Borrowed books successfully: ")

            for book in foundBooks:
                book[4].append(borrower)
                print(book[1] + " - " + book[2])
                rentedISBNs.append(book[0])

            continue
        elif choice == "3" or choice == "T" or choice == "t":
            book_isbn = input("Enter ISBN: ")
            for book in allBooks:
                if book[0] == book_isbn:
                    if book[0] in rentedISBNs:
                        book[4].remove(borrower)
                        rentedISBNs.remove(book[0])
                        print("Book returned successfully.")
                    else:
                        print("No book is found in the borrowed books list!")
                    break
            else:
                print("No book is found in the borrowed books list!")

        elif choice == "4" or choice == "L" or choice == "l":
            printBooks()

        elif choice == "5" or choice == "X" or choice == "x":
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            printBooks()

            exit()


start()
