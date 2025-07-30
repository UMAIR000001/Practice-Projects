<<<<<<< HEAD
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
=======
Project No. 01: Employee Information Search System
Overview
This Python project provides an Employee Information Search System that allows users to quickly retrieve employee details from a given dataset by entering a unique Employee ID. The system leverages a CSV dataset, processes it into an efficient dictionary format for fast lookups, and offers a user-friendly interface to access specific employee data.

Project Features:
CSV Data Processing: The project reads employee data from a CSV file (training_and_development_data.csv) using the pandas library. It simplifies data manipulation and processing for efficient retrieval.
Data Conversion: After loading the data, it is converted into a dictionary format where the Employee ID serves as the key, and employee details (name, position, department, etc.) are stored as nested dictionaries.
Efficient Search: The program implements a highly efficient search algorithm using Python dictionaries, ensuring O(1) lookup time for fast access to employee information.
Interactive Input: Users can input an Employee ID to search for specific employee details. The system responds with the requested information or an error message if the ID is invalid.
Error Handling: If the inputted Employee ID doesn't exist in the dataset, the system displays an appropriate "Employee not found" message, ensuring a smooth user experience.
CSV Dataset Structure: The project assumes that the dataset consists of essential employee details, including Employee ID, Name, Department, and Position.
How It Works:
Input: Users enter an Employee ID when prompted by the program.
Processing: The function get_employee_info() checks if the provided Employee ID exists within the dictionary emp_dict.
Output: If the ID is valid, the program outputs the corresponding employee's details. If the ID is not found, the program returns a message indicating that the employee is not present in the dataset.
Prerequisites:
Python 3.x
pandas library (pip install pandas)
Installation:
To get started with the project, follow the steps below:

Clone this repository:
bash
Copy
Edit
git clone https://github.com/yourusername/employee-information-search.git
Navigate to the project directory:
bash
Copy
Edit
cd employee-information-search
Install required dependencies:
bash
Copy
Edit
pip install pandas
Place your CSV file (training_and_development_data.csv) in the same directory as the Python script or modify the file path in the code.
Run the Python script:
bash
Copy
Edit
python employee_search.py
Example of Employee Data:
The CSV file should have at least the following columns:

Employee ID
Name
Department
Position
Example Output:
Input:

yaml
Copy
Edit
Enter Employee ID: 1001
Output:

bash
Copy
Edit
{'Employee ID': 1001, 'Name': 'John Doe', 'Department': 'HR', 'Position': 'Manager'}
Input:

yaml
Copy
Edit
Enter Employee ID: 5000
Output:

bash
Copy
Edit
Employee not found
Contributing:
Feel free to fork this repository, make changes, and submit pull requests to enhance the project. Any suggestions or improvements are welcome!

.
>>>>>>> project1/main
