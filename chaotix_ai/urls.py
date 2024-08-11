from django.contrib import admin
from django.urls import path
from imagegen.views import generate_images_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-images/', generate_images_view, name='generate_images'),
]
