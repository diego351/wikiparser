# -*- coding: utf-8 -*-
import logging
import sys

from lib.wikipediaresolver import WikipediaResolver
from lib.prettyfier import Prettyfier

__author__ = 'jnowak'

logging.basicConfig(format='%(message)s', level=logging.DEBUG)

try:
    finish_at = sys.argv[2]

except IndexError:
    finish_at = 'Straż Pożarna'

try:
    start_from = sys.argv[1]

except IndexError:
    logging.error('Usage: python parse.py <start_from> <finish_at> (optional)')
    exit()

resolver = WikipediaResolver(start_from, finish_at)
links = resolver.solve()
Prettyfier.print_nicely(links)

