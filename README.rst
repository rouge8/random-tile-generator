random-tile-generator
=====================

Generate random tile layouts, e.g. for backsplash, bathrooms, etc.

Installation
------------

With uv:
^^^^^^^^

1. ``uv sync``

With mise:
^^^^^^^^^^

1. ``mise trust``
2. ``mise run setup``

Usage
-----

.. code-block:: sh

   uv run random-tile-generator PATH_TO_CONFIG PATH_TO_OUTPUT

Configuration
-------------

See ``example.toml``.

Development
-----------

Development tools and dependencies are managed with `mise
<https://mise.jdx.dev/>`_. Run ``mise run setup`` to install all tools and
dependencies.

Keeping up to date with the template
------------------------------------

.. code-block:: sh

   # Add the 'template' remote if necessary
   git remote get-url template || git remote add template git@github.com:rouge8/python-template.git

   # Fetch and merge the latest changes
   git fetch template
   git merge template/main

   # Resolve any merge conflicts, run the tests, commit your changes, etc.
