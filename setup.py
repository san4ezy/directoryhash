# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

setup(
    name="directoryhash",
    version=__import__('directoryhash').__version__,
    description=open(os.path.join(os.path.dirname(__file__), "DESCRIPTION")).read(),
    license="The MIT License (MIT)",
    keywords="directoryhash, directory_hash, hash of directory, directory md5, directory sha1, folder hash, "
             "md5 folder, sha1 folder",

    author="Alexander Yudkin",
    author_email="alexander@yudkin.com.ua",

    maintainer="Alexander Yudkin",
    maintainer_email="alexander@yudkin.com.ua",

    url="http://yudkin.com.ua",
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
