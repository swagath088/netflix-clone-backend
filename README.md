📌 Netflix Clone Backend (Django)

This repository contains the backend for a Netflix Clone web application built using Django and Django REST Framework.
It provides REST APIs for user authentication and movie management.

🚀 Features
🔐 User Authentication

User registration and login

Role-based access (normal users & admin users)

Secure logout functionality

🎬 Movie Management

Browse movies by category (Action, Romance, Web Series, etc.)

View movie details

Search movies by name

Movie data stored with image and video URLs

🛠 Admin Functionality

Admin users can add, update, and delete movies

Content managed through the Django admin panel

🧰 Tech Stack

Backend: Django, Django REST Framework

Database: PostgreSQL (Neon – cloud hosted)

Media Storage: Cloudinary

Deployment:

Backend: Render

Frontend: Vercel

⚙️ Setup Instructions (Local)
1. Clone the repository
git clone https://github.com/swagath088/netflix-clone-backend.git
cd netflix-clone-backend

2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Create superuser
python manage.py createsuperuser

6. Run the server
python manage.py runserver


Access the admin panel at:

http://127.0.0.1:8000/admin/

🌐 Live Deployment

Backend deployed on Render

Frontend deployed on Vercel

This backend works in conjunction with the Netflix Clone frontend to provide a complete full-stack streaming platform experience.