# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Django_C'
copyright = '2025, Zohaib Muhammad'
author = 'Zohaib Muhammad'
release = '1.0'

# -- Django Integration ------------------------------------------------------
# Ensures Django is properly set up for documentation generation

import os
import sys
import django

sys.path.insert(0, os.path.abspath('..'))  # Adjust path if needed
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')  # Ensure this matches your actual project name

django.setup()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      # Automatically generate documentation from docstrings
    'sphinx.ext.viewcode',     # Adds links to source code
    'sphinx.ext.napoleon'      # Supports Google & NumPy-style docstrings
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Output directory configuration -----------------------------------------
# Ensures generated documentation is stored in a dedicated folder

html_output_path = '../docs'  # Stores documentation in the `docs` folder


