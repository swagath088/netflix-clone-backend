# Netflix Clone Backend (Django)

This is the backend for a Netflix Clone application, built using Django and Django REST Framework. It provides API endpoints for managing users, movies, images, and videos.

---

## Features

- **User Authentication**
  - Register, Login, Logout
  - Superuser privileges to add, modify, or delete movies
- **Movie Management**
  - Movies stored with images and video links
  - REST API endpoints for frontend consumption
- **Admin Features**
  - Superuser can manage all movies and media directly

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** MySQL (or SQLite for local testing)
- **Image Handling:** Pillow
- **MySQL Driver:** PyMySQL

---

## Prerequisites

- Python 3.13+
- MySQL server (if using MySQL)
- Virtual environment (`venv`)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/swagath088/netflix-clone-backend.git
cd netflix-clone-backend

2. Create a virtual environment and install dependencies
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
3. Database setup
python manage.py makemigrations
python manage.py migrate
4. Media sample

Add small sample media to demonstrate the app:
media_sample/
├── images/
│   └── sample.jpg
└── movies/
    └── sample.mp4
5. Create a superuser
python manage.py createsuperuser
6. Run the server
python manage.py runserver
Access the Django admin panel at: http://127.0.0.1:8000/admin/

Notes

Pillow must be installed to handle image fields.

PyMySQL is used as the MySQL driver for Django.

This backend works with the Netflix Clone frontend.