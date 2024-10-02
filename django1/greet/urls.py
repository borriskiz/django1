from django.urls import path
from greet.views import index


urlpatterns = [
    path("", index),
]