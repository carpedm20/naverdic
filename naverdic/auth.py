# -*- coding: utf-8 -*-

"""
naverdic.auth
~~~~~~~~~~~~~

This module provides an authentication for NAVER account.
"""
import execjs

def login(account, password):

    js_path = os.path.join(os.path.dirname(__file__), 'login.long.js')

    with open(js_path) as f:
        js = f.read()

    execjs.eval(js)


    pass
