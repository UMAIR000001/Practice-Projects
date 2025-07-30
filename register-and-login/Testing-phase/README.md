# Flask Authentication Application

A secure and modular Flask web application with user authentication features. This application provides a robust foundation for building web applications with user management capabilities.

## Features

- User registration and login system
- Secure password hashing
- Form validation and CSRF protection
- Session management
- Error handling
- Modular blueprint structure
- Environment-based configuration
- PostgreSQL database integration

## Prerequisites

- Python 3.7 or higher
- PostgreSQL database
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Windows
set SECRET_KEY=your-secure-secret-key
set DATABASE_URL=postgresql://username:password@localhost:5432/flask_auth

# Linux/Mac
export SECRET_KEY=your-secure-secret-key
export DATABASE_URL=postgresql://username:password@localhost:5432/flask_auth
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Project Structure

```
├── auth/                    # Authentication blueprint
│   ├── __init__.py         # Blueprint initialization
│   └── routes.py           # Authentication routes
├── templates/              # HTML templates
│   ├── auth/              # Authentication templates
│   └── errors/            # Error templates
├── static/                # Static files (CSS, JS, images)
├── app.py                 # Application factory
├── config.py              # Configuration settings
├── extensions.py          # Flask extensions
├── forms.py               # Form classes
├── models.py              # Database models
└── requirements.txt       # Project dependencies
```

## Running the Application

1. Start the development server:
```bash
python app.py
```

2. Access the application at `http://localhost:5000`

## Configuration

The application supports different configurations:

- Development: `config['development']`
- Production: `config['production']`
- Default: `config['default']`

To switch configurations, modify the `config_name` parameter in `create_app()`.

## Security Features

- Password hashing using Werkzeug
- CSRF protection
- Form validation
- Secure session management
- Environment variable configuration
- SQL injection prevention through SQLAlchemy

## Error Handling

The application includes custom error pages for:
- 404 Not Found
- 500 Internal Server Error

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers. 