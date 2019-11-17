=====
Usage
=====

To use django-vadmin in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'vadmin',
        ...
    )

Add django-vadmin's URL patterns:

.. code-block:: python

    from vadmin import urls as vadmin_urls


    urlpatterns = [
        ...
        url(r'^', include(vadmin_urls)),
        ...
    ]
