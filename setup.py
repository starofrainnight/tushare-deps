#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file, open('HISTORY.rst') as history_file:
    long_description = (readme_file.read() + "\n\n" + history_file.read())

tushare_requires = [
    # Because tushare library does not setup correct library dependences, so
    # we have to add library dependences here for complete the library search
    # behavior.
    'lxml',
    'pandas',
    'beautifulsoup4',
    'requests',
]

install_requires = [
    *tushare_requires,
    'tushare',
]

setup_requires = [
    *tushare_requires,
    'pytest-runner',
]

tests_requires = [
    'pytest',
]

setup(
    name='tushare-deps',
    version='0.0.2',
    description="A library prepare the dependences for tushare library",
    long_description=long_description,
    author="Hong-She Liang",
    author_email='starofrainnight@gmail.com',
    url='https://github.com/starofrainnight/tusharedeps',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license="Apache Software License",
    zip_safe=False,
    keywords='tusharedeps',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=tests_requires,
    setup_requires=setup_requires,
)
