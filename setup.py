import os
from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.txt')) as f:
    README = f.read()

with open('requirements.txt') as f:
    require = f.readlines()

with open('tests_requirements.txt') as f:
    tests_require = f.readlines()

setup(
    name="multipserve",
    version="1.0.4",
    author="Mario Idival",
    author_email="marioidival@gmail.com",
    description=("Script for using with multiples applications Pyramid"),
    long_description=README,
    license="BSD",
    keywords="multipserve pyramid threading",
    url="https://github.com/marioidival/multipserve",
    scripts=['multipserve/bin/mpserve'],
    packages=['multipserve'],
    install_requires=require,
    tests_require=tests_require,
    test_suite='tests',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Framework :: Pyramid",
        "Operating System :: Unix",
    ],
)
