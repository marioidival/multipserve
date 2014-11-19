import os
from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.rst')) as f:
    README = f.read()

setup(
    name="multipserve",
    version="1.0.6",
    author="Mario Idival",
    author_email="marioidival@gmail.com",
    description=("Script for using with multiples applications Pyramid"),
    long_description=README,
    license="BSD",
    keywords="multipserve pyramid threading",
    url="https://github.com/marioidival/multipserve",
    packages=['multipserve'],
    install_requires=[],
    tests_require=['nose', 'coverage'],
    test_suite='tests',
    entry_points={
        'console_scripts': ['mpserve=multipserve.mpserve:main']
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Framework :: Pyramid",
        "Operating System :: Unix",
    ],
)
