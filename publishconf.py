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
# English feeds (at root)
FEED_ALL_ATOM = "feeds/all.atom.xml"          # All posts (all languages mixed)
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"            # All posts (all languages mixed)
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

# Note: Portuguese feeds are configured in pelicanconf.py I18N_SUBSITES
# They will be at: pt/feeds/all.atom.xml and pt/feeds/all.rss.xml

# Optional: Limit number of items in feeds
FEED_MAX_ITEMS = 20

DELETE_OUTPUT_DIRECTORY = True
