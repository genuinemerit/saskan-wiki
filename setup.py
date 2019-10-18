# coding: utf-8

"""
Ball of Wax Wiki

:Contact: genuinemerit @ pm.me

To install BowWiki library:

``` bash
    cd to ~/bow/bow-wiki
    run ``sudo pip install -e .``
```

"""

from setuptools import setup, find_packages

NAME = "BowWiki"
VERSION = "0.1.0"
REQUIRES = [
    'pprint'
]

setup(
    name=NAME,
    version=VERSION,
    description="Ball of Wax Wiki",
    long_description="""
    This is a collection of wiki pages, mostly markdown, providing information about the Ball of Wax projects.
    """,
    author_email="genuinemerit@pm.me",
    url="",
    keywords=["BoW", "wiki"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    project_urls={
        "Documentation": "https://github.com/genuinemerit/bow-wiki",
        "Source": "https://github.com/genuinemerit/bow-wiki",
        "Project kanban": "https://github.com/users/genuinemerit/projects/1"
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Linux",
        "Programming Language :: Python3",
    ]
)
