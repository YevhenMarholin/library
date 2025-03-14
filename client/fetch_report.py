import requests

BASE_URL = "http://127.0.0.1:5000"  # Server URL


def search_books():
    """Allow user to search books by author or title."""
    print("\n Search Books")
    author = input("Enter author name (or press Enter to skip): ").strip()
    title = input("Enter book title (or press Enter to skip): ").strip()

    params = {}
    if author:
        params["author"] = author
    if title:
        params["title"] = title

    response = requests.get(f"{BASE_URL}/books", params=params)

    if response.status_code == 200:
        books = response.json()
        print("\n Books Found:")
        for book in books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
        return books
    else:
        print("\n No books found.")
        return []


def rent_book():
    """Allow user to rent a book by choosing ID and entering rental dates."""
    print("\n Rent a Book")
    book_id = input("Enter book ID: ").strip()
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    payload = {"id": int(book_id), "start_date": start_date, "end_date": end_date}
    response = requests.post(f"{BASE_URL}/rent", json=payload)

    if response.status_code == 200:
        print(" Book rented successfully!")
    else:
        print(" The book is already rented for these dates.")


def main_menu():
    """Display the menu and handle user input."""
    while True:
        print("\n Library Client")
        print("1. Search books")
        print("2. Rent a book")
        print("3. Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            search_books()
        elif choice == "2":
            rent_book()
        elif choice == "3":
            print("\n Exiting Library Client. Goodbye!")
            break
        else:
            print(" Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
