# Quora  - Django Project

This is a simple Q&A website inspired by Quora, built using Django. It allows users to register, post questions, answer others' questions, and like answers.

## 🔧 Features

- User registration and login
- Post questions
- View all posted questions
- Answer questions
- Like answers
- Logout functionality

## 🚀 Tech Stack

- Django 4.x
- Python 3.8+
- HTML (Basic)
- Django Forms

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/quora.git
cd quora

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
