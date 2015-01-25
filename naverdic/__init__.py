# -*- coding: utf-8 -*-
"""
naverdic NAVER dictionary library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

naverdic is an unofficial library, written in Python, for human beings.

    >>> import naverdic
    >>> dic = naverdic.Dictionary()
    >>> search = dic.search('carpe diem')

:copyright: (c) 2015 by Taehoon Kim.
:license: Apache 2.0, see LICENSE for more details.
"""

__title__ = 'naverdic'
__version__ = '0.0.1'
__author__ = 'Taehoon Kim'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015 Taehoon Kim'
__author_email__ = 'carpedm20@gmail.com'
__url__ = 'http://github.com/carpedm20/naverdic'

from .dictionary import Dictionary
