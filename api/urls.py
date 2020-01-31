from rest_framework import routers
from api.views import NavBarItemsViewSet, ServicesViewSet, all_doctors
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'all/navbar-items', NavBarItemsViewSet)
router.register(r'services', ServicesViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path(r'all-doctors/', all_doctors),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)