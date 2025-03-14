This project is a simple **Flask-based server** and **Python client** that allows users to:
- Search for books by **author** or **title**.
- Rent a book if it is available.
- Track the number of API requests and reset the counter.

Install dependencies
Make sure you have **Python 3.10+** installed. Then install the required packages:
```sh
pip install -r requirements.txt

2️⃣ Run the Server
cd server
python server.py

 API Endpoints
1. Search for books
GET /books?author=Taras Shevchenko
GET /books?title=Kobzar

2. Rent a book
POST /rent
Content-Type: application/json

3. Get request count
GET /count-requests

4. Reset request counter
POST /reset-counter


Running the Client
cd client
python fetch_report.py
