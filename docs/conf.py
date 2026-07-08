project = 'FamilySearch-login'
author = 'FamilySearch-login'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Bing search verification
html_context = {
    <meta name="msvalidate.01" content="8CB3D830D2E0EFAE9978E877D3E9887C" />
}

# Base URL for sitemap
html_baseurl = 'https://FamilySearchlogin.readthedocs.io/en/latest/'
