from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login_site, name = 'login'),
    path('signup/',views.signup, name = 'signup'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.edit_profile, name = 'profile'),
    path('password_reset/', views.PasswordReset.as_view(), name = 'pwreset')
]
