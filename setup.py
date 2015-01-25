#!/usr/bin/env python

import os
import sys

import naverdic

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'naverdic',
]

requires = [
    'requests',
]

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='naverdic',
    version=naverdic.__version__,
    description='NAVER dictionary wrapper for Python',
    long_description=readme,
    author='Taehoon Kim',
    author_email='carpedm20@gmail.com',
    url='http://github.com/carpedm20/naverdic',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'naverdic': 'naverdic'},
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
