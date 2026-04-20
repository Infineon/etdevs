"""Configuration file for the Sphinx documentation builder."""

import os
import sys

# If extensions are in another directory, add it to sys.path
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information
project = "etdevs"
copyright = "2026, Infineon Technologies"
author = "Infineon Technologies"
release = "0.1.0"

# -- General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx_tabs.tabs",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "logo_only": False,
    "collapse_navigation": True,
}

# MyST configuration
myst_enable_extensions = ["colon_fence"]
