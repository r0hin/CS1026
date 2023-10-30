"""
  CS1026a 2023
  Assignment 02
  Rohin Arya
  251371185
  rarya4
  Oct 12, 2023
"""

# initial list of books
allBooks = [
    ["9780596007126", "The Earth Inside Out", "Mike B", 2, ["Ali"]],
    ["9780134494166", "The Human Body", "Dave R", 1, []],
    ["9780321125217", "Human on Earth", "Jordan P", 1, ["David", "b1", "user123"]],
]

# list of rented books
rentedISBNs = []

# Prints the main menu
def printMenu():
    print("\n######################")
    print("1: (A)dd a new book.")
    print("2: Bo(r)row books.")
    print("3: Re(t)urn a book.")
    print("4: (L)ist all books.")
    print("5: E(x)it.")
    print("######################\n")

# Checks if the ISBN is valid
def isValidISBN(isbn):
    if len(isbn) != 13: # ISBN must be 13 digits long.
        return False
    if not isbn.isnumeric(): # ISBN must be numeric.
        return False
    
    # Chech matching the required sum of digits
    checksum = 0
    for i in range(0, len(isbn)):
        if i % 2 == 1: # Odd index
            checksum += int(isbn[i]) * 3
        else:
            checksum += int(isbn[i])

    if checksum % 10 == 0: # Checksum must be divisible by 10.
        return True
    return False

# Prints all books
def printBooks():
    for book in allBooks:
        # Loop through all books and print them.
        print("---------------")
        if book[0] in rentedISBNs:
            print("[Unavailable]")
        else:
            print("[Available]")
        print(book[1] + " - " + book[2])
        print("E: " + str(book[3]) + " ISBN: " + book[0])
        print("borrowed by: " + str(book[4]))

# Handles choice 1 ( Add a new book )
def handleChoiceOne():
    book_name = input("Book name> ")
    while True: # Check if book name contains * or %
        if "*" in book_name or "%" in book_name:
            print("Invalid book name!")
            book_name = input("Book name> ")
        else:
            break # Break if no * or % is found.
    book_author = input("Author name> ")
    book_edition = input("Edition> ")
    while True: # Check if book edition is numeric.
        if book_edition.isnumeric():
            break
        else:
            print("Invalid edition!") # If not numeric, try again
            book_edition = input("Edition> ")
    # Consider only the numeric part of book_edition
    book_edition = int(book_edition)
    while True:
        book_isbn = input("ISBN: ")
        # If non-numeric characters are present.
        if not book_isbn.isnumeric() or len(book_isbn) != 13:
            print("Invalid ISBN!")
        else:
            if isValidISBN(book_isbn): # Check if ISBN is valid.
                # Check if already exists.
                for book in allBooks:
                    if book[0] == book_isbn:
                        print("Duplicate ISBN is found! Cannot add the book.")
                        break
                else:  # Triggered if for loop doesnt break.
                    allBooks.append(
                        [book_isbn, book_name, book_author, book_edition, []]
                    ) # Add the book to the list.
                    print("A new book is added successfully.")
                break
            else:
                print("Invalid ISBN. Returning to menu.")
                break; # Break if ISBN is invalid.

# Handles choice 2 ( Borrow books )
def handleChoiceTwo():
    # Inputs
    borrower = input("Enter the borrower name> ")
    search_term = input("Search term> ").lower()

    # Check if search term contains * or %
    if search_term[len(search_term) - 1] == "*":
        # Contains mode
        search_term = search_term[:-1] # Remove the * from the end
        foundBooks = []

        for book in allBooks:
            if search_term in book[1].lower(): # Check if search term is in book name
                foundBooks.append(book)

    elif search_term[len(search_term) - 1] == "%":
        # Starts with mode 
        search_term = search_term[:-1] # Remove the % from the end
        foundBooks = []

        for book in allBooks:
            if book[1].lower().startswith(search_term): # Check if book name starts with search term
                foundBooks.append(book)
    else:
        # Exact match mode
        foundBooks = []
        for book in allBooks:
            if search_term == book[1].lower(): # Check if book name is equal to search term
                foundBooks.append(book)

    # Filter out books that are already rented.
    for book in foundBooks:
        if book[0] in rentedISBNs:
            foundBooks.remove(book)

    # Borrow all foundBooks
    if not len(foundBooks):
        print("No books found!")

    for book in foundBooks:
        book[4].append(borrower)
        # Add the book to the rented list
        rentedISBNs.append(book[0])
        print('-"' + book[1] + '" is borrowed!')

# Handles choice 3 ( Return books )
def handleChoiceThree():
    # Inputs
    book_isbn = input("ISBN> ")
    for book in allBooks: # Check all books
        if book[0] == book_isbn: # If book ISBN matches
            if book[0] in rentedISBNs: # If ISBN already rented
                rentedISBNs.remove(book[0]) # Remove from rented list
                print('"' + book[1] + '" is returned.')
            else: # If ISBN is not rented
                print("No book is found in the borrowed books list!")
            break
    else: # If book is not found
        print("No book is found!")

# Main function
def start():
    while True: # While loop can be exited via break or exit()
        printMenu()
        choice = input("Your selection> ")
        # Check num, capital letters or lowercase letters
        if choice == "1" or choice == "A" or choice == "a":
            handleChoiceOne()
        elif choice == "2" or choice == "R" or choice == "r":
            handleChoiceTwo()
        elif choice == "3" or choice == "T" or choice == "t":
            handleChoiceThree()
        elif choice == "4" or choice == "L" or choice == "l":
            printBooks()
        elif choice == "5" or choice == "X" or choice == "x":
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            printBooks()
            break
        else:
            # Invalid choice
            print("Wrong selection! Please selection a valid option.")

# Start the program
start()
