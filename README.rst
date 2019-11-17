=============================
django-kradmin
=============================

.. image:: https://badge.fury.io/py/django-kradmin.svg
    :target: https://badge.fury.io/py/django-kradmin

.. image:: https://travis-ci.org/bushig/django-kradmin.svg?branch=master
    :target: https://travis-ci.org/bushig/django-kradmin

.. image:: https://codecov.io/gh/bushig/django-kradmin/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/bushig/django-kradmin

Your project description goes here

Documentation
-------------

The full documentation is at https://django-kradmin.readthedocs.io.

Quickstart
----------

Install django-kradmin::

    pip install django-kradmin

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'kradmin',
        ...
    )

Add django-kradmin's URL patterns:

.. code-block:: python

    from kradmin import urls as kradmin_urls


    urlpatterns = [
        ...
        url(r'^', include(kradmin_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
