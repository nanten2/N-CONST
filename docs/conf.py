import os
import re
import sys
import ast

sys.path.insert(0, os.path.abspath("../n_const"))

with open(os.path.abspath("../pyproject.toml")) as f:
    match = re.search(r"version\s+=\s+(.*)", f.read())
version = str(ast.literal_eval(match.group(1)))

# -- Project information -----------------------------------------------------

project = "N-CONST"
copyright = "2021, NANTEN2 software team"
author = "NANTEN2 software team"

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "m2r2",
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/nanten2/N-CONST/",
}
html_logo = "_static/logo.svg"
html_sidebars = {
    "**": [
        "sidebar-nav-bs.html",
        "sidebar-search-bs.html",
    ],
}

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
