# -*- coding: utf-8 -*-
import logging

import requests
from pyquery import PyQuery as PQ

from treelib import Tree
__author__ = 'jnowak'


class WikipediaResolver(object):
    """ WikipediaResolver class
    """
    _base_wiki_url = 'https://pl.wikipedia.org'
    _base_wiki_url_search = _base_wiki_url + '/wiki/'

    def __init__(self, start_from, finish_at):
        """
        :param start_from: Wikipedia entry like "Chrześcijaństwo"
        :param finish_at: Wikipedia entry like "Biblia"
        :return: WikipediaResolver instance
        """
        self._tree = Tree()
        self._finish_at_url = requests.get(self._base_wiki_url_search + finish_at).url
        self._to_check_list = [(None, self._base_wiki_url_search + start_from)]
        self._known_resources = set()

    def solve(self):
        """
        :return: returns ordered list (start point first) of found links (steps)
        """
        while True:
            found_node = self._process_level()
            if found_node:
                break

        # logging.debug("Formating tree... This may take a while.")
        # self._show_tree()

        path = self._backtrack_path()

        return path

    def _process_level(self):
        """
        :return: Bool. True if target link was found in dispached breadth graph search iteration, else False
        """
        to_check_list = []
        while self._to_check_list:
            parent_url, url = self._to_check_list.pop(0)
            self._known_resources.add(url)

            if not parent_url:
                self._tree.create_node(url, url)  # this is root node

            set_to_check = set((self._base_wiki_url + a.attr('href') for a in self._get_a_items(requests.get(url).text) if a.attr('href')))

            set_to_check -= self._known_resources

            map((lambda _url: self._tree.create_node(_url, _url, parent=url)), set_to_check)

            if self._finish_at_url in set_to_check:
                return True

            to_check_list += [(url, _url) for _url in set_to_check]
            self._known_resources.update(set_to_check)

        self._to_check_list += to_check_list

    def _show_tree(self):
        """ This simply print current state of the tree
        :return: Nothing
        """
        self._tree.show()

    def _backtrack_path(self):
        """ Backtracks found link among the tree.
        :return: returns ordered list (start point first) of found links (steps)
        """
        node = self._tree.get_node(self._finish_at_url)
        nodes = [node]

        while node.bpointer:
            nodes.append(self._tree.get_node(node.bpointer))
            node = self._tree.get_node(node.bpointer)

        return list(reversed([node.identifier for node in nodes]))

    @staticmethod
    def _get_a_items(html):
        dom = PQ(html)  # this parses html into tree
        return dom.find('a[href^="/wiki/"]:not([href*=":"])').items()  # Neat jquery style selectors. #PDK
