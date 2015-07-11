#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='flamework.api',
    namespace_packages=['flamework', 'flamework.api', 'flamework.api.client', 'flamework.api.request'],
    version='0.2',
    description='Simple Python wrapper for Flamework derived APIs',
    author='Aaron Straup Cope',
    url='https://github.com/straup/py-flamework-api',
    install_requires=[
        'requests',
        ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/straup/py-flamework-api/releases/tag/v0.2',
    license='BSD')
