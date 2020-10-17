#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: nujnus
# Mail: 50191646@qq.com
#############################################
  
from setuptools import setup, find_packages

setup(
    name = "climate",
    version = "0.1",
    keywords = ("pip", "climate"),
    description = "mini cliui framework",
    long_description = "mini cliui framework",
    license = "MIT Licence",

    url = "",
    author = "nujnus",
    author_email = "50191646@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    scripts = ['bin/climate']
)
