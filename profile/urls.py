from django.urls import path
from .views import upload_file, showImage
urlpatterns=[
    path('upload_file/',upload_file, name='upload_file'),
    path('showImage/', showImage, name='showImage'),
    ]