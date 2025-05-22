# Configuration file for the Sphinx documentation builder.
#
# Documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project Information -----------------------------------------------------
import os
import sys
import django

sys.path.insert(0, os.path.abspath('../../'))   # Ensure the project root is in the path
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'  # Set correct module
django.setup()


project = 'Django_C'
copyright = '2025, Zohaib Muhammad'
author = 'Zohaib Muhammad'
release = '1.0'

# -- General Configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',       # Automatically document modules
    'sphinx.ext.intersphinx',    # Link to other documentation sources
    'sphinx.ext.napoleon',       # Support for Google-style docstrings
    'sphinx.ext.viewcode'        # Add links to highlighted source code
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML Output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Autodoc Settings --------------------------------------------------------
autodoc_default_options = {
    'members': True,             # Document all class members
    'undoc-members': True,       # Include members without docstrings
    'show-inheritance': True,    # Show class inheritance diagrams
}

# -- Intersphinx Mapping -----------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'django': ('https://docs.djangoproject.com/en/stable/', None),
}

