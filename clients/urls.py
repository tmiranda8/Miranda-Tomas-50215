from django.urls import path
from clients import views

urlpatterns = [
    path('list/', views.ClientsList.as_view(), name='clientslist'),
    path('new/', views.NewClient.as_view(), name='newclient'),
    path('<int:pk>/details/', views.ClientDetails.as_view(), name='clientdetails'),
    path('<int:pk>/delete/',views.DeleteClient.as_view(), name='deleteclient'),
    path('<int:pk>/edit/',views.EditClient.as_view(), name='editclient')
]
