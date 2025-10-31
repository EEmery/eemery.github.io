# pelicanconf.py

# --- Core Settings ---
AUTHOR = "Operator"
SITENAME = "Robots and Coffee Co."
# SITEURL = "robotsandcoffee.co"
SITEURL = ""
TIMEZONE = "Europe/London"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# --- Paths and URLs ---
PATH = "content"
ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]

# Ignore hidden files and IDE directories
IGNORE_FILES = ['.#*', '__pycache__', '*.pyc', '*~', '.*']

# Tell Pelican to use your custom theme
THEME = "theme"

# --- Language & Translation (i18n) ---
DEFAULT_LANG = "en"
PLUGINS = ["i18n_subsites", "webassets"] # Enable plugins
JINJA_ENVIRONMENT = {}
I18N_TEMPLATES_LANG = "en" # Default language for templates

I18N_SUBSITES = {
    "pt": {
        "SITENAME": "Robos e Café",
        "DEFAULT_LANG": "pt",
        "MENUITEMS": (
            ("Logs", "pt/logs.html"),
            ("Info", "pt/pages/info.html"),
        ),
    }
}

# --- Page & Menu Setup ---
# 1. "Logs" page (list of all articles)
DIRECT_TEMPLATES = ["index"]
INDEX_SAVE_AS = "logs.html" # Save the article list as logs.html
PAGINATED_TEMPLATES = {"index": None}

# 2. "Info" page (and top menu)
DISPLAY_PAGES_ON_MENU = False # We want a custom menu
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ("Logs", "logs.html"),
    ("Info", "pages/info.html"),
)

# 3. No Author Pages
AUTHOR_SAVE_AS = ""  # Disables generating author pages
AUTHORS_SAVE_AS = ""

# --- Static Files Configuration ---
# Copy static files (js, images, etc.) to output
STATIC_PATHS = ['static']

# --- Webassets Configuration ---
WEBASSETS_SOURCE_PATHS = ['static']
WEBASSETS_CONFIG = [
    ('libsass_style', 'compressed'),
]

# --- Feed Generation (Optional) ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
