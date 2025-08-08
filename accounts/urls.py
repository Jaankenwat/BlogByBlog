from django.urls import path
from accounts import views
urlpatterns = [
    path('sign-up/', views.SignUp,name='SignUp'),
    path('login/', views.Login,name='Login'),
    path('logout/', views.Logout,name='Logout'),
    
    
]
