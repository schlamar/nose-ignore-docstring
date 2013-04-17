Nose ignore docstrings
======================

This is a plugin for nose. If this plugin is active, nose doesn't use
docstrings to name tests.


Installation
------------

You can install or upgrade ``nose-ignore-docstring`` with these commands::

  $ pip install nose-ignore-docstring
  $ pip install --upgrade nose-ignore-docstring



Usage
-----

Pass the ``--with-ignore-docstrings`` option to ``nosetests``::

    $ nosetests --with-ignore-docstrings -v
    ...

Or define the following entry in ``setup.cfg``::

    [nosetests]
    with-ignore-docstrings=1


Changes
-------


0.1 - 2013-04-17
````````````````
* First release
