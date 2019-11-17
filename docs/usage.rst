=====
Usage
=====

To use django-kradmin in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'kradmin.apps.KradminConfig',
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
