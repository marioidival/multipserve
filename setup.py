import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name = "multipserve",
    version = "0.0.1",
    author = "Mario Idival",
    author_email = "marioidival@gmail.com",
    description = ("Script for using with multiples applications Pyramid"),
    license = "BSD",
    keywords = "multipserve pyramid threading",
    url = "https://github.com/marioidival/multi_pserve",
    packages=['multi_pserve'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
