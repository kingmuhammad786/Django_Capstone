Django Capstone Project - Portfolio App
🔹 Author: Zohaib 🔹 Technologies: Django, Docker, Sphinx Documentation 🔹 Hosted on: Docker Playground

📌 Project Overview
This is a portfolio project built with Django, allowing users to showcase projects and interact with polls. The project is containerized using Docker for easy deployment and includes well-documented code using Sphinx.

🛠 Setup Instructions
✅ Using a Virtual Environment (venv)
1️⃣ Clone the repository:


git clone <https://github.com/kingmuhammad786/Django_Capstonek>
cd Django_Capstone
2️⃣ Create & activate a virtual environment:


python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install dependencies:


pip install -r requirements.txt
4️⃣ Run migrations:


python manage.py migrate
5️⃣ Start the Django server:


python manage.py runserver
6️⃣ Open in your browser: Navigate to:

http://localhost:8000
🐳 Using Docker (Recommended)
This project is containerized using Docker, making it easy to deploy.

1️⃣ Clone the repository:


git clone <https://github.com/kingmuhammad786/Django_Capstone>
cd Django_Capstone
2️⃣ Build the Docker container:


docker build --no-cache -t django-capstone .
3️⃣ Run the container:


docker run -p 8000:8000 django-capstone
4️⃣ Access the application: If using Docker Playground, navigate to port 8000 in your browser.

📜 Project Structure
Django_Capstone/
│── portfolio_project/   # Django project settings
│── portfolio/           # Portfolio app with models, views, templates
│── docs/                # Sphinx-generated documentation
│── static/              # Static assets (CSS, JavaScript, images)
│── templates/           # HTML templates
│── Dockerfile           # Containerization setup
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation
│── .gitignore           # Files to exclude from version control
🔒 Security Considerations
✔ Sensitive Data: Ensure .env files store secrets securely. ✔ Database: Default SQLite, but can be swapped for PostgreSQL. ✔ Static & Media Files: Set up proper configurations in settings.py.

📜 Documentation
This project is fully documented using Sphinx. To generate documentation locally:


cd docs
make html
Then, open:

docs/_build/html/index.html

📌 https://github.com/kingmuhammad786/Django_Capstone