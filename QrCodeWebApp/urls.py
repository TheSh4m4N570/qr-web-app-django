from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('qrapp.urls')),
    path('admin/', admin.site.urls),
]
