#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-wish',
    version='0.6.1',
    author='Alessandro Amici',
    author_email='alexamici@gmail.com',
    maintainer='Alessandro Amici',
    maintainer_email='alexamici@gmail.com',
    license='MIT',
    url='https://github.com/alexamici/pytest-wish',
    download_url='https://github.com/alexamici/pytest-wish/archive/0.6.1.tar.gz',
    description='Test-Driven no-Development plugin for pytest',
    long_description=read('README.rst'),
    packages=find_packages(),
    py_modules=['all'],
    install_requires=[
        'pytest>=2.8.1',
        'future',
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'wish = pytest_wish',
        ],
    },
)
