# -*- coding: utf-8 -*-

"""
naverdic.dictionary
~~~~~~~~~~~~~~~~~~~
This module provides a Dictionary object to send NAVER dictionary APIs.

"""
import requests

from .auth import login

def Dictionary(object):
    """A NAVER dictionary.

    Send NAVER dictionary APIs.
    
    Basic Usage::

        >>> import naverdic
        >>> dic = naverdic.Dictionary()
        >>> dic.search('carpe diem')
        success
        >>> dic = naverdic.Dictionary('NAVER_ID','NAVER_PASSWORD')
        >>> wordbooks = dic.get_wordbooks()
    """

    __attrs__ = [
        'session',
    ]

    def __init__(self, account="", password=""):
        if account:
            session, success = login(account, password)

            if success:
                self.session = session
            else:
                raise ("NAVER login failed.")
        else:
            #: A Requests session.
            self.session = requests.Session()

        #: Do we success NAVER login?
        self.login = False


    def search(self, word, language="en"):
        """Search meanings of word for specific language dictionary.

        :param word: a word to search.
        :param language: (optional) which dictionary to find.
        """
        pass
