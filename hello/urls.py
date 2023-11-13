from django.urls import path
from .views import hello_world, intro

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('intro/', intro, name='intro'),
]