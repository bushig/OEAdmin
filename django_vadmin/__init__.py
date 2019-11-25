# ACTION_CHECKBOX_NAME is unused, but should stay since its import from here
# has been referenced in documentation.
from django_vadmin.decorators import register
from django_vadmin.filters import (
    AllValuesFieldListFilter, BooleanFieldListFilter, ChoicesFieldListFilter,
    DateFieldListFilter, FieldListFilter, ListFilter, RelatedFieldListFilter,
    RelatedOnlyFieldListFilter, SimpleListFilter,
)
from django_vadmin.helpers import ACTION_CHECKBOX_NAME
from django_vadmin.options import (
    HORIZONTAL, VERTICAL, ModelAdmin, StackedInline, TabularInline,
)
from django_vadmin.sites import AdminSite, site
from django.utils.module_loading import autodiscover_modules

# __all__ = [
#     "register", "ACTION_CHECKBOX_NAME", "ModelAdmin", "HORIZONTAL", "VERTICAL",
#     "StackedInline", "TabularInline", "AdminSite", "site", "ListFilter",
#     "SimpleListFilter", "FieldListFilter", "BooleanFieldListFilter",
#     "RelatedFieldListFilter", "ChoicesFieldListFilter", "DateFieldListFilter",
#     "AllValuesFieldListFilter", "RelatedOnlyFieldListFilter", "autodiscover",
# ]


def autodiscover():
    autodiscover_modules('vadmin', register_to=site)


default_app_config = 'django_vadmin.apps.VadminConfig'


__version__ = '0.1.0'


# Version synonym
VERSION = __version__
