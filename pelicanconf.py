#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'San Diego Python'
SITENAME = u'San Diego Python'
SITEURL = 'http://pythonsd.org'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

TEMPLATE_PAGES = {
    'static/home.html': 'index.html',
}

# Social widget
# Icons are in themes/sandiegopython/static/images/icons
SOCIAL = (
    ('meetup', 'http://meetup.com/pythonsd'),
    ('twitter', 'http://twitter.com/sandiegopython'),
    ('google group', 'https://groups.google.com/group/pythonsd'),
    ('github', 'http://github.com/pythonsd'),
    ('irc', 'irc://irc.freenode.net/sandiegopython'),
)

DEFAULT_PAGINATION = 10

THEME = "themes/sandiegopython"

FEED_ATOM = "feeds/posts.atom.xml"

JINJA_EXTENSIONS = (
    'jinja2.ext.loopcontrols',
)
