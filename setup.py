#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='flamework.api',
    namespace_packages=['flamework', 'flamework.api', 'flamework.api.client', 'flamework.api.request'],
    version='0.1',
    description='Simple Python wrapper for Flamework derived APIs',
    author='Smithsonian Cooper-Hewitt National Design Museum',
    url='https://github.com/cooperhewitt/py-flamework-api',
    install_requires=[
        'requests',
        ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-flamework-api/releases/tag/v0.1',
    license='BSD')
