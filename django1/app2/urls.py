from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = 'app2_index'),
    path("1", views.do1, name = 'app2_1'),
    path("2", views.do2, name = 'app2_2'),
    path("3", views.do3, name = 'app2_3'),
]
