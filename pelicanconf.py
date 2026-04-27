# pelicanconf.py

# --- Core Settings ---
AUTHOR = "Operator"
SITENAME = "Robots and Coffee Co."
# SITEURL = "robotsandcoffee.co"
SITEURL = ""
TIMEZONE = "Europe/London"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

# Site logo for RSS/Atom feeds
SITELOGO = "/theme/images/logo-large.png"
SITELOGO_SIZE = "600"  # Width in pixels (recommended: 512-600)

# --- Paths and URLs ---
PATH = "content"
ARTICLE_PATHS = ["articles", "ephemerals"]
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
            ("Ephm", "pt/ephemerals/"),
            ("Info", "pt/pages/info/"),
        ),
        "STATIC_PATHS": [],  # Don't duplicate static files in pt/
        # Feeds for Portuguese subsite (will be in pt/feeds/)
        "FEED_ALL_ATOM": "feeds/all.atom.xml",
        "FEED_ALL_RSS": "feeds/all.rss.xml",
    }
}

# --- Page & Menu Setup ---
# 1. "Logs" page (list of all articles)
DIRECT_TEMPLATES = ["index", "ephemerals", "404"]
INDEX_SAVE_AS = "index.html" # Save the article list as index.html (root page)
EPHEMERALS_SAVE_AS = "ephemerals/index.html"
PAGINATED_TEMPLATES = {"index": None, "ephemerals": None}

# 404 page (GitHub Pages will automatically use this)
TEMPLATE_PAGES = {"404.html": "404.html"}

# 2. "Info" page (and top menu)
DISPLAY_PAGES_ON_MENU = False # We want a custom menu
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ("Logs", ""),
    ("Ephm", "ephemerals/"),
    ("Info", "pages/info/"),
)

# 3. No Author/Category Pages
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

# --- Static Files Configuration ---
# Copy static files (js, images, videos, etc.) to output
STATIC_PATHS = ["static", "images", "videos", "extra/CNAME"]

# Keep images at root level, not inside language subdirectories
STATIC_EXCLUDE_SOURCES = False
STATIC_CREATE_LINKS = False
STATIC_CHECK_IF_MODIFIED = False

# Copy CNAME file to root for custom domain
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

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
