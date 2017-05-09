========================
Python Biased Stop Words
========================

.. image:: https://badge.fury.io/py/biased-stop-words.svg
    :target: https://badge.fury.io/py/biased-stop-words

.. image:: http://img.shields.io/badge/license-MIT-yellow.svg?style=flat
    :target: https://github.com/gregology/python-biased-stop-words/blob/master/LICENSE

.. image:: https://img.shields.io/badge/contact-Gregology-blue.svg?style=flat
    :target: http://gregology.net/contact/

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

``biased-stop-words`` is available on PyPI

http://pypi.python.org/pypi/biased-stop-words

So easily install it by ``pip``
::

    $ pip install biased-stop-words

Or by ``easy_install``
::

    $ easy_install biased-stop-words

Another way is by cloning ``biased-stop-words``'s `git repo <https://github.com/gregology/python-biased-stop-words>`_ ::

    $ git clone --recursive git://github.com/gregology/python-biased-stop-words.git

Then install it by running:
::

    $ python setup.py install

Basic usage
-----------
::

    from biased_stop_words import get_stop_words

    stop_words = get_stop_words('en-gendered')


Python compatibility
--------------------

Python-stop-words has been originally developed for Python 2, but has been
ported and tested for Python 3.
