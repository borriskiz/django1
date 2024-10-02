from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = 'app1_index'),
    path("1", views.do1, name = 'app1_1'),
    path("2", views.do2, name = 'app1_2'),
    path("3", views.do3, name = 'app1_3'),
]