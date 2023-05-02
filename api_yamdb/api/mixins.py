from rest_framework import filters, mixins, viewsets

from .permissions import IsAdminOnly, ReadOnly


class CRDViewSet(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet
                 ):
    """mixin for category and genre viewsets."""
    permission_classes = (IsAdminOnly | ReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
