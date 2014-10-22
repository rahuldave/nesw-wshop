#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Author'
SITENAME = u'Site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#specific
THEME = './pelican-bootstrap3-modified'
BOOTSTRAP_THEME = 'flatly'
TWITTER_USERNAME="Author"

# Blogroll
LINKS =  (('Piazza', 'https://piazza.com/harvard/spring2014/am207/home'),
          ('Videos', 'http://cm.dce.harvard.edu/2014/02/24104/publicationListing.shtml'),
          ('ISite', 'http://isites.harvard.edu/icb/icb.do?keyword=k102129&login=yes'),)

OTHERLINKS = (('Numpy', 'http://docs.scipy.org/doc/numpy/reference/'),
          ('Scipy', 'http://docs.scipy.org/doc/scipy/reference/'),
          ('Pandas', 'http://pandas.pydata.org/pandas-docs/dev/'),
          ('Matplotlib', 'http://matplotlib.org/api/index.html'),
          ('PyMC3', 'https://github.com/pymc-devs/pymc'),
          ('IACS', 'http://iacs.seas.harvard.edu'),)

# Social widget
SOCIAL = True

DEFAULT_PAGINATION = 10
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
NEWEST_FIRST_ARCHIVES = True

USE_FOLDER_AS_CATEGORY=False
#MENU
DISPLAY_PAGES_ON_MENU=False
DISPLAY_CATEGORIES_ON_MENU=False

ARTICLEDIR='posts'
PAGEDIR='pages'
PAGE_EXCLUDES=('othermd',)
ARTICLE_EXCLUDES=('pages','othermd',)
#categiries: homework, lecture, lab, project

start = SITEURL
def do_menuitems(start):
    menuitems = [
          ('Schedule', "%s/schedule.html" % start ),
          ('Syllabus', "%s/syllabus.html" % start ),
          ('Policies', "%s/policies.html" % start ),
          ('Resources', "%s/resources.html" % start ),
          ('Contact', "%s/contact.html" % start ),
          ]
    return menuitems

INTERLINKS = {
    'wikipedia_en': 'http://en.wikipedia.org/wiki/',
    'wikipedia_es': 'http://es.wikipedia.org/wiki/',
    'ddg': 'https://duckduckgo.com/?q='
}
PLUGIN_PATH = './pelican-plugins-activated'
PLUGINS = ['interlinks', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.notebook', 'liquid_tags.include_code',
           'liquid_tags.include_md']

EXTRA_HEADER = open('./notebook_header.html').read().decode('utf-8')

STATIC_PATHS=['static', 'images', 'code', 'notebooks', 'files']

#INDEX_SAVE_AS='index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DIRECT_TEMPLATES = ('tags', 'categories', 'authors', 'archives')