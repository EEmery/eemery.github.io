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

# Pretty URLs (remove .html extension)
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

# Ignore hidden files and IDE directories
IGNORE_FILES = ['.#*', '__pycache__', '*.pyc', '*~', '.*']

# Tell Pelican to use your custom theme
THEME = "theme"

PLUGINS = ["i18n_subsites", "webassets"] # Enable plugins

# --- Language & Translation (i18n) ---
DEFAULT_LANG = "en"
JINJA_ENVIRONMENT = {}
I18N_TEMPLATES_LANG = "en" # Default language for templates

I18N_SUBSITES = {
    "pt": {
        "SITENAME": "Robos e Café",
        "DEFAULT_LANG": "pt",
        "MENUITEMS": (
            ("Logs", "pt/"),
            ("Info", "pt/pages/info/"),
        ),
        "STATIC_PATHS": [],  # Don't duplicate static files in pt/
    }
}

# --- Page & Menu Setup ---
# 1. "Logs" page (list of all articles)
DIRECT_TEMPLATES = ["index", "404"]
INDEX_SAVE_AS = "index.html" # Save the article list as index.html (root page)
PAGINATED_TEMPLATES = {"index": None}

# 404 page (GitHub Pages will automatically use this)
TEMPLATE_PAGES = {"404.html": "404.html"}

# 2. "Info" page (and top menu)
DISPLAY_PAGES_ON_MENU = False # We want a custom menu
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ("Logs", ""),
    ("Info", "pages/info/"),
)

# 3. No Author Pages
AUTHOR_SAVE_AS = ""  # Disables generating author pages
AUTHORS_SAVE_AS = ""

# --- Static Files Configuration ---
# Copy static files (js, images, etc.) to output
STATIC_PATHS = ["static", "images"]

# Keep images at root level, not inside language subdirectories
STATIC_EXCLUDE_SOURCES = False
STATIC_CREATE_LINKS = False
STATIC_CHECK_IF_MODIFIED = False

# Images should be referenced from root for all languages
# Use: ![alt text](/images/photo.png) in markdown

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
