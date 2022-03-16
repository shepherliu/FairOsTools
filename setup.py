# setup.py

import os
from setuptools import setup, find_packages

__version__ = '1.0' 

requirements = open('requirements.txt').readlines() 

setup(
    name = 'FairOsTools', 
    version = __version__,
    author = 'shepherliu',
    author_email = 'shepherliu@gmail.com',
    url = 'https://github.com/shepherliu/FairOsTools',
    description = 'FairOs Python Libs',
    packages = find_packages(exclude=[".git"]), 
    python_requires = '>=3.5.0',
    install_requires = requirements 
        )