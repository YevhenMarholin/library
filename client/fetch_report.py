import requests

BASE_URL = "http://127.0.0.1:5000"


def search_books(author=None, title=None):
    """Search for books by author or title"""
    params = {}
    if author:
        params["author"] = author
    if title:
        params["title"] = title

    response = requests.get(f"{BASE_URL}/books", params=params)

    if response.status_code == 200:
        books = response.json()
        print("Found books:")
        for book in books:
            print(f" {book['title']} - {book['author']} (ID: {book['id']})")
    else:
        print("No books found.")


def rent_book(book_id, start_date, end_date):
    """Rent a book by ID"""
    payload = {"id": book_id, "start_date": start_date, "end_date": end_date}
    response = requests.post(f"{BASE_URL}/rent", json=payload)

    if response.status_code == 200:
        print("Book rented successfully!")
    else:
        print("The book is already rented.")


if __name__ == "__main__":
    print("Searching for books by author 'Taras Shevchenko':")
    search_books(author="Taras Shevchenko")

    print("\n Renting book with ID 2 for January:")
    rent_book(2, "2024-01-01", "2024-01-31")
