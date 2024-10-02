from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = 'app3_index'),
    path("1", views.do1, name = 'app3_1'),
    path("2", views.do2, name = 'app3_2'),
    path("3", views.do3, name = 'app3_3'),
]
