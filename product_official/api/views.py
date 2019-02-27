from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import APP, Game, H5, LittleProgram
from .serializer import APPSerializer, ProductSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class AppViewSet(ReadOnlyModelViewSet):
    queryset = APP.objects.all()
    serializer_class = APPSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', )
    filter_fields = ('name', )

class GameViewSet( ReadOnlyModelViewSet):
    queryset = Game.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', )
    filter_fields = ('name', )

class H5ViewSet( ReadOnlyModelViewSet):
    queryset = H5.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', )
    filter_fields = ('name', )

class LittleProgramViewSet(ReadOnlyModelViewSet):
    queryset = LittleProgram.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', )
    filter_fields = ('name', )

