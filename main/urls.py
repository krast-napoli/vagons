from django.urls import path
from . import views

urlpatterns = [
#    path('', views.index, name='index'),
    path('', views.trains_list, name='trains_list'),
    path('', views.create_new, name='create_new')
]
