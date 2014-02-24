import os
from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.txt')) as f:
    README = f.read()



setup(
    name = "multipserve",
    version = "1.0.1aa",
    author = "Mario Idival",
    author_email = "marioidival@gmail.com",
    description = ("Script for using with multiples applications Pyramid"),
    long_description = README,
    license = "BSD",
    keywords = "multipserve pyramid threading",
    url = "https://github.com/marioidival/multi_pserve",
    scripts = ['multi_pserve/bin/multipserve.py'],
    packages=['multi_pserve'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
