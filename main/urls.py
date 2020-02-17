from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
#    path('', views.trains_list, name='trains_list'),
#    path('', views.create_new, name='create_new')
]
