from django.urls import path
from products import views

urlpatterns = [
    path('show/', views.get_database, name="database"),
    path('addnetdevice/', views.set_netdevice, name="netdevice"),
    path('addiotdevice/', views.set_iotdevice, name="iotdevice"),
    path('addhwcomponent/', views.set_hwcomp, name="hardware"),
    path('search/', views.search, name='search'),
    path('products/<int:object_id>/delete/', views.delete, name='delete'),
    path('products/<int:object_id>/update/',views.update, name="update")
]