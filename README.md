# 🎯 Django Capstone Project - Portfolio App

🔹 **Author:** Zohaib  
🔹 **Technologies:** Django, Docker, Sphinx Documentation  
🔹 **Hosted on:** Docker Playground  

---

## 📌 Project Overview
This is a **portfolio project built with Django**, allowing users to showcase projects and interact with polls. The project is containerized using **Docker** for easy deployment and includes well-documented code using **Sphinx**.

---

## 🛠 Setup Instructions

### ✅ Using a Virtual Environment (venv)
1️⃣ **Clone the repository**:
   ```bash
   git clone https://github.com/kingmuhammad786/Django_Capstone
   cd Django_Capstone

2️⃣ Create & activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install dependencies:

bash
pip install -r requirements.txt
4️⃣ Run migrations:

bash
python manage.py migrate
5️⃣ Start the Django server:

bash
python manage.py runserver
6️⃣ Open the application in your browser:

http://localhost:8000
🐳 Using Docker (Recommended)
This project is containerized using Docker, making it easy to deploy.

1️⃣ Clone the repository:

bash
git clone https://github.com/kingmuhammad786/Django_Capstone
cd Django_Capstone
2️⃣ Build the Docker container:

bash
docker build --no-cache -t django-capstone .
3️⃣ Run the container:

bash
docker run -p 8000:8000 django-capstone
4️⃣ Access the application: If using Docker Playground, navigate to port 8000 in your browser.

📜 Project Structure
Django_Capstone/
├── portfolio_project/   # Django project settings
├── portfolio/           # Portfolio app (models, views, templates)
├── docs/                # Sphinx-generated documentation
│   ├── conf.py
│   ├── _build/html/     # (Generated documentation output)
│   └── index.html
├── static/              # Static assets (CSS, JavaScript, images)
├── templates/           # HTML templates
├── Dockerfile           # Containerization setup
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
├── .gitignore           # Files to exclude from version control
🔒 Security Considerations
✔ Sensitive Data: Ensure .env files store secrets securely. ✔ Database: Default is SQLite, but can be swapped for PostgreSQL. ✔ Static & Media Files: Proper configurations are set in settings.py.

📜 Accessing Documentation
This project includes pre-generated documentation using Sphinx.

✅ How to View the Documentation
1️⃣ Navigate to the docs/_build/html/ folder. 2️⃣ Open the index.html file in your browser.

Regenerate Documentation (Optional)
If needed, you can regenerate the documentation manually:

bash
cd docs
sphinx-build -b html source _build/html
Then, open:

docs/_build/html/index.html
📌 Repository Link
🔗 https://github.com/kingmuhammad786/Django_Capstone