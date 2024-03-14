from django.urls import path
from clients import views

urlpatterns = [
    path('list/', views.Read.as_view(), name='listview'),
    path('create/', views.Create.as_view(), name='createview'),
    path('<int:pk>/details/', views.Details.as_view(), name='detailview'),
    path('<int:pk>/delete/',views.Delete.as_view(),name='deleteview'),
    path('<int:pk>/update/',views.Update.as_view(),name='updateview')
]
