reStructuredText
Django_C Documentation
======================

Welcome to the official documentation for the **Django Capstone Project**.  
This guide provides details on **setup, features, API usage, and deployment**.

Overview
--------
The Django Capstone Project is a web application designed to **showcase portfolio projects** and allow user interaction.  
It is containerized using **Docker** and includes well-documented code using **Sphinx**.

Installation & Setup
---------------------
Follow these steps to install and run the application:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kingmuhammad786/Django_Capstone
   cd Django_Capstone
Activate the virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
Install dependencies:

bash
pip install -r requirements.txt
Run database migrations:

bash
python manage.py migrate
Start the development server:

bash
python manage.py runserver
Features

✔ User authentication and profile management ✔ Project showcase with descriptions and images ✔ Interactive polling system ✔ API integration for external services ✔ Responsive design for web & mobile

API Endpoints

The application includes several API endpoints for interacting with user data and projects.

GET /api/projects/ → Returns a list of portfolio projects

POST /api/projects/ → Adds a new project

PUT /api/projects/<id>/ → Updates an existing project

DELETE /api/projects/<id>/ → Removes a project

Usage Guidelines

After setting up the project, you can: ✔ Create a new project profile using the dashboard. ✔ Participate in polls and interact with user portfolios. ✔ Manage user authentication through Django’s built-in system.

Documentation Access

This project includes pre-generated documentation using Sphinx.

📌 How to View the Documentation: 1️⃣ Navigate to the docs/_build/html/ folder. 2️⃣ Open the index.html file in your browser.

.. toctree:: :maxdepth: 2 :caption: Contents:

installation features api usage documentation



