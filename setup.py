# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

setup(
    name="<package_name>",
    version=__import__('<package_name>').__version__,
    description=open(os.path.join(os.path.dirname(__file__), "DESCRIPTION")).read(),
    license="The MIT License (MIT)",
    keywords="<keywords>",

    author="<name>",
    author_email="<email>",

    maintainer="<name>",
    maintainer_email="<email>",

    url="<site_url>",
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)