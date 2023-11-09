from django.urls import path
from sites import views
from sites import views

urlpatterns = [
    path('showdatabase/', views.get_database, name="database"),
    path('addnetdevice/', views.set_netdevice, name="netdevice"),
    path('addiotdevice/', views.set_iotdevice, name="iotdevice"),
    path('addhwcomponent/', views.set_hwcomp, name="hardware"),
    path('search/', views.get_device, name='search')
]