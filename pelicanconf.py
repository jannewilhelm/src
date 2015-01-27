#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Janne Wilhelm'
SITENAME = 'Janne Wilhelm, Psychotherapie und Beratung'
SITENAME_PRINT = 'Janne Wilhelm'
SITEURL = 'http://192.168.178.23:8000'
#SITEURL = 'http://jannewilhelm.neocities.org'

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'de' # warum war das auskommentiert?
# not working yet
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'de': '%a %m.%d.%Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#REVERSE_CATEGORY_ORDER = True
#DEFAULT_CATEGORY = 'Willkommen'

DELETE_OUTPUT_DIRECTORY = True
# FILES_TO_COPY = ()

TYPOGRIFY = True

#PAGE_PATHS = ['pages']

#THEME = "theme/notmyidea-cms"
#THEME = "theme/sneakyidea"
#THEME = "theme/simple-bootstrap"
#THEME = "theme/subtle"
THEME = "theme/myown"

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# my markdown extensions reside in d:/py/blogtools, which must be on PYTHONPATH for this to work
MD_EXTENSIONS = ['markdown.extensions.toc', 'standout', 'custom_span_class']

