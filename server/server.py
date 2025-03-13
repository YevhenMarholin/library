from flask import Flask, jsonify, request

app = Flask(__name__)

# Request counter
request_counter = 0  

# Book database (Ukrainian books and authors)
books = [
    {"id": 1, "author": "Lesia Ukrainka", "title": "Lisova pisnia"},
    {"id": 2, "author": "Taras Shevchenko", "title": "Kobzar"},
    {"id": 3, "author": "Ivan Franko", "title": "Zakhar Berkut"},
    {"id": 4, "author": "Mykhailo Kotsiubynskyi", "title": "Tini zabutykh predkiv"},
    {"id": 5, "author": "Panteleimon Kulish", "title": "Chorna rada"}
]

# Rental database
rentals = {}


@app.route('/books', methods=['GET'])
def get_books():
    """Retrieve a list of books by author or title"""
    author = request.args.get('author')
    title = request.args.get('title')

    filtered_books = books
    if author:
        filtered_books = [book for book in books if book['author'].lower() == author.lower()]
    if title:
        filtered_books = [book for book in filtered_books if book['title'].lower() == title.lower()]

    if not filtered_books:
        return jsonify({"message": "No books found"}), 404

    return jsonify(filtered_books)


@app.route('/rent', methods=['POST'])
def rent_book():
    """Rent a book by its ID"""
    data = request.get_json()
    book_id = data.get('id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if book_id in rentals:
        return jsonify({"message": "The book is already rented for these dates"}), 400

    rentals[book_id] = {"start_date": start_date, "end_date": end_date}
    return jsonify({"message": "Book rented successfully"}), 200


@app.route('/count-requests', methods=['GET'])
def count_requests():
    """Increment request counter and return current count"""
    global request_counter
    request_counter += 1
    return jsonify({'request_count': request_counter})


@app.route('/reset-counter', methods=['POST'])
def reset_requests():
    """Reset request counter to zero"""
    global request_counter
    request_counter = 0
    return jsonify({'message': 'Counter reset successfully'})


if __name__ == '__main__':
    app.run(debug=True)
