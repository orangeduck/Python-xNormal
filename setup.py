#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xNormal",
    version="1.1.0",
    author="Daniel Holden, Paul Greveson",
    author_email="contact@theorangeduck.com",
    description="Wrapper for xNormal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orangeduck/Python-xNormal",
    packages=setuptools.find_packages(),
)