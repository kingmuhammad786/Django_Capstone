# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Django_C'
copyright = '2025, Zohaib Muhammad'
author = 'Zohaib Muhammad'
release = '1.0'

# -- Django Integration ------------------------------------------------------
import os
import sys
import django

# 🔹 Explicitly set Django settings module 🔹
os.environ["DJANGO_SETTINGS_MODULE"] = "portfolio_project.settings"

# 🔹 Modify sys.path to ensure Django project is correctly detected 🔹
project_root = os.path.abspath("C:/Users/zohai/Django_Consilidation")
sys.path.insert(0, project_root)  # Parent directory of `portfolio_project`

django.setup()  # Initializes Django AFTER sys.path is correctly set

# ✅ DEBUGGING TEST: Print Python module search path
print("DEBUG: Python sys.path (inside Sphinx):")
for path in sys.path:
    print("  -", path)

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Output directory configuration -----------------------------------------
html_output_path = '../docs'  # Stores documentation in the `docs` folder









