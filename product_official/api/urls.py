from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, GameViewSet, H5ViewSet, LittleProgramViewSet

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Product official API')

router = DefaultRouter()
router.register('app', AppViewSet)
router.register('game', GameViewSet)
router.register('h5', H5ViewSet)
router.register('littleprogram', LittleProgramViewSet)

urlpatterns = [
    url(r'^docs/', schema_view),
]

urlpatterns += router.urls

# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]


# from django.conf.urls import url
#
# from . import views
#
# app_name = 'api'
# urlpatterns = [
#     url(r'^insert/', views.insert),
#     url(r'^query/', views.query),
#     # url(r'', views.hello),
# ]