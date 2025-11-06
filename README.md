# Learning Log

A Django web application for logging topics and entries about what you're learning.

## Features

- Create and manage learning topics
- Add entries for each topic with detailed notes
- Edit existing entries
- View all topics and their associated entries
- Clean, simple interface for tracking your learning progress

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd learning_log
```

2. Create a virtual environment:
```bash
python -m venv ll_env
source ll_env/bin/activate  # On Windows: ll_env\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your browser

## Usage

- Navigate to `/topics/` to view all topics
- Click on a topic to see its entries
- Use "Add new topic" to create a new learning topic
- Use "Add new entry" within a topic to log what you've learned
- Edit entries using the "edit entry" link

## Project Structure

- `learning_logs/` - Main application containing models, views, and templates
- `learning_log/` - Project configuration
- `db.sqlite3` - SQLite database (not tracked in git)
- `manage.py` - Django management script

## Technologies

- Python 3.12
- Django 5.2.7
- SQLite
