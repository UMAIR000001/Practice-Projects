# Book Store Receipt Generator

A simple Flask-based web application that generates receipts for book purchases. This application allows users to select books from a predefined list and generates a detailed receipt with the total amount.

## Features

- Display a list of available books with prices
- Allow users to select quantities for each book
- Generate detailed receipts with itemized lists
- Calculate total purchase amount
- Clean and simple user interface

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/receipt_generator.git
cd receipt_generator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required dependencies:
```bash
pip install flask
```

## Project Structure

```
receipt_generator/
├── app.py              # Main Flask application
├── books.py           # Book and Receipt classes
├── templates/         # HTML templates
│   ├── index.html    # Main page template
│   └── receipt.html  # Receipt template
└── README.md         # Project documentation
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Select the quantity of books you want to purchase

4. Click the "Generate Receipt" button to view your receipt

## Features in Detail

- **Book Selection**: Choose from a curated list of popular books
- **Quantity Selection**: Select the number of copies for each book
- **Receipt Generation**: Get a detailed receipt with individual items and total
- **Error Handling**: Built-in validation for quantity inputs

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. You can also open issues for any bugs found or feature suggestions.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 