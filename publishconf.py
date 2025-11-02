# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://robotsandcoffee.co"
RELATIVE_URLS = False

# --- Feed Configuration ---
# ATOM feeds
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = "feeds/all-{lang}.atom.xml"

# RSS feeds
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
TRANSLATION_FEED_RSS = "feeds/all-{lang}.rss.xml"

# Optional: Limit number of items in feeds
FEED_MAX_ITEMS = 20

DELETE_OUTPUT_DIRECTORY = True
