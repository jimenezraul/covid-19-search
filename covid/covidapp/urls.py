from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('covid_search/', views.covid_search, name='covid_search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
