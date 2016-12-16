*************
DirectoryHash
*************

DirectoryHash is a library for Python. It gives an opportunity to get a hash of the destination folder. You can choose file types, which will participate in the calculations.

`Github repo <https://github.com/san4ezy/directoryhash>`_

Installation
============

Install using pip::

    pip install directoryhash

...or clone the project from github::

    https://github.com/san4ezy/directoryhash.git


How to use?
===========

Getting hash for whole directory::

    from directoryhash import md5, sha1

    md5_hash = md5("path_to_directory")
    sha1_hash = sha1("path_to_directory")


Getting hash for directory including html and css only::

    from directoryhash import md5, sha1

    filetypes = ('.html', '.css',)

    md5_hash = md5("path_to_directory", filetypes)
    sha1_hash = sha1("path_to_directory", filetypes)
