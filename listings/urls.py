from django.urls import path
from .views import listing, submissions, updateTask, deleteTask, contact
urlpatterns=[
    path('listing/',listing, name='listing'),
    path('submissions/', submissions, name='submissions'),
    path('updatepg/<str:pk>/', updateTask, name='updatepg'),
    path('deletepg/<str:pk>/', deleteTask, name='deletepg'),
    path('contact/<str:id>', contact, name='contact'),
    ]