# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

try:
    long_description = open("README.md").read()
except IOError:
    long_description = """
"""

setup(
    name="dockerify",
    version="0.1.1",
    description="Dockerify - tooling for generating dockerfile",
    license="MIT",
    author="Alex Myasoedov",
    author_email="msoedov@gmail.com",
    packages=['dockerify'],
    install_requires=['trafaret'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)