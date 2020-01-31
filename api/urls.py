from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('all-doctors/', views.AllDoctors.as_view()),
    path('all-navbar-items/', views.NavBarItemsViewSet.as_view()),
    path('services/', views.ServicesViewSet.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)