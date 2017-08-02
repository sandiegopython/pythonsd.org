#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'San Diego Python'
SITENAME = u'San Diego Python'
SITEURL = 'http://www.pythonsd.org'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

TEMPLATE_PAGES = {
    'static/home.tpl': 'index.html',
}

# Social widget
# Icons are in themes/sandiegopython/static/images/icons
SOCIAL = (
    ('meetup', 'http://meetup.com/pythonsd'),
    ('twitter', 'http://twitter.com/sandiegopython'),
    ('google group', 'https://groups.google.com/group/pythonsd'),
    ('github', 'http://github.com/pythonsd'),
    ('irc', 'irc://irc.freenode.net/sandiegopython'),
    ('slack', 'https://pythonsd.slack.com/'),
)

DEFAULT_PAGINATION = 10

THEME = "themes/sandiegopython"

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/posts.atom.xml'
FEED_RSS = 'feeds/posts.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

JINJA_ENVIRONMENT = {
    'extensions': (
        'jinja2.ext.loopcontrols',
    ),
    'trim_blocks': True,
    'lstrip_blocks': True,
}

STATIC_PATHS = ['images']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
