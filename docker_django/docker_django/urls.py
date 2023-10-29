from django.urls import path
from django.contrib import admin
from api_index.views import citation_aleatoire

urlpatterns = [
    path('', citation_aleatoire, name='citation_aleatoire'),
    path('admin/', admin.site.urls),
]
