# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://robotsandcoffee.co"
RELATIVE_URLS = False

# Logo for RSS/Atom feeds (absolute URL for feed readers)
SITELOGO = "https://robotsandcoffee.co/theme/images/logo-large.png"

# --- Feed Configuration ---
# Mixed language feeds (all posts from all languages)
FEED_ALL_ATOM = "feeds/all.atom.xml"          # All posts (EN + PT mixed)
FEED_ALL_RSS = "feeds/all.rss.xml"            # All posts (EN + PT mixed)
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

# Language-specific feeds (English-only)
TRANSLATION_FEED_ATOM = "feeds/{lang}.atom.xml"   # English: feeds/en.atom.xml
TRANSLATION_FEED_RSS = "feeds/{lang}.rss.xml"     # English: feeds/en.rss.xml

# Note: Portuguese feeds are configured in pelicanconf.py I18N_SUBSITES
# Portuguese-only feeds: pt/feeds/all.atom.xml and pt/feeds/all.rss.xml

# Optional: Limit number of items in feeds
FEED_MAX_ITEMS = 20

DELETE_OUTPUT_DIRECTORY = True
