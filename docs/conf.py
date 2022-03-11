import n_const

print(n_const.__file__)


# -- Project information -----------------------------------------------------

project = "N-CONST"
copyright = "2021-2022, NANTEN2 software team"
author = "NANTEN2 software team"
release = version = n_const.__version__

# -- General configuration ---------------------------------------------------

extensions = [
    "m2r2",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autosummary_generate = True
add_module_names = False
autodoc_member_order = "bysource"
autodoc_typehints_format = "short"
autodoc_typehints = "description"
napoleon_use_ivar = True

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/nanten2/N-CONST",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/n-const/",
            "icon": "fas fa-cubes",
            "type": "fontawesome",
        },
    ],
    "navbar_start": ["navbar-logo"],
}
# html_logo = "_static/logo.svg"
html_favicon = "https://avatars.githubusercontent.com/u/20414019?s=400&u=0e47c7d5efc6cf27086c8cfcdb6fd5c757926043&v=4"  # noqa: E501
html_sidebars = {
    "**": [
        "version",
        "search-field.html",
        "sidebar-nav-bs.html",
    ],
}

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
