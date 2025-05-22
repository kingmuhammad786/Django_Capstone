Installation Guide
==================

Follow these steps to install the Django_C project:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/kingmuhammad786/Django_Capstone.git
   ```
   Navigate to the project directory:

   ```bash
   cd Django_Capstone
   ```


2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```



