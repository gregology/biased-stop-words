========================
Python Biased Stop Words
========================

.. contents:: Table of contents

Overview
--------

Get lists of biased stop words from various genres.
Based on http://pypi.python.org/pypi/stop-words

Available genres
----------------

* English Gendered Terms

Installation
------------

by cloning ``biased-stop-words``'s `git repo <https://github.com/gregology/python-biased-stop-words>`_ ::

Basic usage
-----------
::

    from biased_stop_words import get_stop_words

    stop_words = get_stop_words('en-gendered')


Python compatibility
--------------------

Python-stop-words has been originally developed for Python 2, but has been
ported and tested for Python 3.
