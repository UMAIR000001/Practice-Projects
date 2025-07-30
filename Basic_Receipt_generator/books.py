class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Receipt:
    def __init__(self):
        self.items = []

    def add_item(self, book, quantity):
        total = book.price * quantity
        self.items.append({
            'title': book.title,
            'price': book.price,
            'quantity': quantity,
            'total': total
        })

    def calculate_total(self):
        return sum(item['total'] for item in self.items)
