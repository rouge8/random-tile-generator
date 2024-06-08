random-tile-generator
=====================

Generate random tile layouts, e.g. for backsplash, bathrooms, etc.

Installation
------------

1. Create a virtualenv.
2. ``pip install -r requirements.txt``

Usage
-----

.. code-block:: sh

   random-tile-generator PATH_TO_CONFIG PATH_TO_OUTPUT

Configuration
-------------

See ``example.toml``.

Keeping up to date with the template
------------------------------------

.. code-block:: sh

   # Add the 'template' remote if necessary
   git remote get-url template || git remote add template git@github.com:rouge8/python-template.git

   # Fetch and merge the latest changes
   git fetch template
   git merge template/main

   # Resolve any merge conflicts, run the tests, commit your changes, etc.
