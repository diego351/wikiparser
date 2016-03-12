# -*- coding: utf-8 -*-
import urllib

__author__ = 'jnowak'

class Prettyfier(object):
    @classmethod
    def print_nicely(cls, links):
        """ Prints links according to the task.
        :param links: List of Wikipedia links
        :return: Nothing
        """

        for idx, link in enumerate(links):
            print "%s. %s" % (idx + 1, cls.get_article_name(link))
            print "%s\n" % (link,)

    @classmethod
    def get_article_name(self, link):
        """ This is a bit haxy but does the job.
        :param link: Wikipedia link
        :return: String
        """
        url_encoded = link.split('/wiki/')[-1]
        return urllib.unquote(url_encoded).replace("_", " ").capitalize()

