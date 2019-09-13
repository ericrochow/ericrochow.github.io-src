#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = "Eric Rochow"
SITEURL = "https://ericroc.how"
SITENAME = AUTHOR
SITETITLE = AUTHOR
# SITESUBTITLE = ""
# SITEDESCRIPTION = ""
SITELOGO = SITEURL + "/images/face.png"
# FAVICON = SITEURL + ""
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.now().year

PATH = "content"

TIMEZONE = "America/Detroit"

DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "Flex"

# PLUGINS = [
# "liquid_tags",
# "pin_to_top",
# "related_posts",
# "similar_posts",
# "pelican-githubprojects",
# "video_privacy_enhancer",
# "goodreads_activity",
# ]
JINJA_EXTENSIONS = []

ROBOTS = "index, follow"
STATIC_PATHS = ["images", "extra/robots.txt", "extra/favicon.ico"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Blogroll
LINKS = (
    # ("Pelican", "http://getpelican.com/"),
    # ("Python.org", "http://python.org/"),
    # ("Jinja2", "http://jinja.pocoo.org/"),
    # ("You can modify those links in your config file", "#"),
    # ("Find Me on the Tubes!", "#"),
)

# Social widget
SOCIAL = (
    ("globe fa-lg", "#"),
    ("envelope-o fa-lg", "mailto:ericrochow@gmail.com"),
    ("rss fa-lg", "#"),
    ("linkedin fa-lg", "https://www.linkedin.com/in/erochow/"),
    ("github fa-lg", "https://github.com/ericrochow"),
    ("reddit fa-lg", "#"),
    ("twitter fa-lg", "https://twitter.com/eric_rochow"),
    ("lastfm fa-lg", "https://www.last.fm/user/ericrochow"),
    (
        "spotify fa-lg",
        "https://open.spotify.com/user/ericrochow?si=KEmxAAk8QZy31L82MMge4g",
    ),
    ("book fa-lg", "https://www.goodreads.com/user/show/18841479-eric-rochow"),
)

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

GOOGLE_ANALYTICS = "UA-135617138-1"
GITHUB_URL = "https://github.com/ericrochow"
GITHUB_USERNAME = "ericrochow"
TWITTER_USERNAME = "eric_rochow"

DEFAULT_PAGINATION = 10

IGNORE_FILES = [".#*", ".swp", ".tmpl"]
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
