from django.urls import path
from  . import views

urlpatterns= [
    path('', views.index,name='index'),
    path('registration/', views.registration, name='registeration'),
    path('maps', views.maps, name='maps'),
]