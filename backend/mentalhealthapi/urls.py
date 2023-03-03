from django.urls import path

from .views import MusicAPI

urlpatterns = [
    path('music', MusicAPI.as_view()),
]