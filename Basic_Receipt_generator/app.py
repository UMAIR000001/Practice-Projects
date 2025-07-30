from flask import Flask, render_template, request
from books import Book, Receipt as BookReceipt  # import Book and Receipt from books.py

app = Flask(__name__)

# Sample book list
books = [
    Book("Think and Grow Rich", 600),
    Book("Rich Dad and Poor Dad", 800),
    Book("Ego is your Biggest Enemy", 750),
    Book("The 7 Habits of Highly Effective People", 650),
    Book("Atomic Habits", 900)
]

@app.route('/', methods=['GET', 'POST'])
def index():
    receipt = BookReceipt()
    total = 0

    if request.method == 'POST':
        for i, book in enumerate(books):
            quantity_str = request.form.get(f'quantity{i}', '0').strip()

            try:
                quantity = int(quantity_str) if quantity_str else 0
            except ValueError:
                quantity = 0

            if quantity > 0:
                receipt.add_item(book, quantity)

        total = receipt.calculate_total()
        return render_template('receipt.html', receipt=receipt.items, total=total)

    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
