# Option 1: Add a book
def add_book(books):
    print("\n--- Add a New Book ---")

    title = input("Enter book title: ")
    author = input("Enter book author: ") 
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower()

    if read == "yes":
        read_status = True
    else:
        read_status = False

    new_book = {
        "Title": title,
        "Author": author,
        "Publication Year": year,
        "Genre": genre,
        "Read Status": read_status
    }

    books.append(new_book)  # ✅ fixed typo
    print("Book added successfully!\n")


# Option 2: Remove a book 
def remove_book(books):
    print("\n--- Remove a Book ---")
    title = input("Enter the title of the book to remove: ")

    found = False
    for book in books:
        if book["Title"].lower() == title.lower():
            books.remove(book)
            print("Book removed successfully!\n")
            found = True
            break
    if not found:
        print("Book not found.\n")


# Placeholder functions
def search_book(books):
    print("\n--- Search for a Book ---")
    query = input("Enter book title or author to search: ").strip().lower()
    found = False

    for book in books:
        if query in book["Title"].lower() or query in book["Author"].lower():
            print(f"\nTitle: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Year: {book['Publication Year']}")
            print(f"Genre: {book['Genre']}")
            print(f"Read: {'Yes' if book['Read Status'] else 'No'}")
            found = True

    if not found:
        print("No matching books found.")

def display_books(books):
    print("\n--- All Books in Library ---")
    if not books:
        print("No books in the library yet.")
        return

    for idx, book in enumerate(books, start=1):
        print(f"\nBook #{idx}")
        print(f"Title: {book['Title']}")
        print(f"Author: {book['Author']}")
        print(f"Year: {book['Publication Year']}")
        print(f"Genre: {book['Genre']}")
        print(f"Read: {'Yes' if book['Read Status'] else 'No'}")

def display_stats(books):
    print("\n--- Library Statistics ---")
    total = len(books)
    if total == 0:
        print("No books in the library.")
        return

    read_books = sum(1 for book in books if book["Read Status"])
    percent_read = (read_books / total) * 100

    print(f"Total books: {total}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percent_read:.2f}%")

def app_exit():
    print("Exiting program...")
    exit()


# Main Menu Function
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1- Add a Book")
        print("2- Remove a Book")
        print("3- Search a Book")
        print("4- Display all Books")
        print("5- Display Statistics of reads")
        print("6- Exit")
        
        select_option = input("Please choose an option (1-6): ")

        if select_option == "1":
            add_book(books)
        elif select_option == "2":
            remove_book(books)
        elif select_option == "3":
            search_book(books)
        elif select_option == "4":
            display_books(books)
        elif select_option == "5":
            display_stats(books)
        elif select_option == "6":
            app_exit()
        else:
            print("Invalid choice. Please try again.")


# Book List
books = [
    {
        "Title": "To Kill a Mockingbird",
        "Author": "Harper Lee",
        "Publication Year": 1960,
        "Genre": "Fiction",
        "Read Status": True
    },
    {
        "Title": "1984",
        "Author": "George Orwell",
        "Publication Year": 1949,
        "Genre": "Dystopian",
        "Read Status": True
    },
    {
        "Title": "The Great Gatsby",
        "Author": "F. Scott Fitzgerald",
        "Publication Year": 1925,
        "Genre": "Classic",
        "Read Status": False
    },
    {
        "Title": "The Catcher in the Rye",
        "Author": "J.D. Salinger",
        "Publication Year": 1951,
        "Genre": "Coming-of-Age",
        "Read Status": False
    }
]

# Run the application
main_menu()
