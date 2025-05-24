Django_Capstone - Portfolio & Polling System
**Author:** Zohaib  
**Technologies:** Django, Docker, Sphinx Documentation  
**Hosted on:** Docker Playground  



📌 Project Overview
Django_Capstone is a web application designed to allow users to showcase projects while engaging with polls for interactive voting. Built using Django, this platform provides a structured way to manage portfolios and user-driven decision-making through polls. The project is containerized using Docker for easy deployment and includes detailed documentation generated with Sphinx.


🚀 Features

🗳 Poll System – Users can vote on different choices.

📦 Portfolio Management – Users can showcase and manage their projects.

🛠 Dockerized Deployment – Ensures consistent environments.

📜 Sphinx Documentation – Easily accessible reference guides.



🛠 Installation Guide
Using a Virtual Environment (venv)

1️⃣ Clone the repository :
git clone https://github.com/kingmuhammad786/Django_Capstone.git
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

6️⃣ Open the application in your browser:
http://localhost:8000(provided in termonal )



🐳 Using Docker (Recommended)
This project is containerized using Docker, making it easy to deploy.

1️⃣ Clone the repository:
git clone https://github.com/kingmuhammad786/Django_Capstone
cd Django_Capstone

2️⃣ Build the Docker container:
docker build --no-cache -t django-capstone .

3️⃣ Run the container:
docker run -p 8000:8000 django-capstone

4️⃣ Access the application: 
If using Docker Playground, navigate to port 8000 in your browser.


🔒 Security Considerations
✔ Sensitive Data: Ensure .env files store secrets securely.
✔ Database: Default is SQLite, but can be swapped for PostgreSQL.
✔ Static & Media Files: Proper configurations are set in settings.py.


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

📌 Repository Link :
🔗 https://github.com/kingmuhammad786/Django_Capstone
