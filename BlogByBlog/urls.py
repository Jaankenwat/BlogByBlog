"""
URL configuration for BlogByBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name='Home'),
    path('auth/',include('accounts.urls') ),
    path('tinymce/', include('tinymce.urls')), 
    path('post/',include('posts.urls') ),
    path('posts/all-posts/', views.all_Post, name='all_Posts'),
    path('about-me/', views.AboutMe,name='about_me'),
    path('contacts/', views.Contacts,name='contacts'),
    path('privacyPolicy/', views.PrivacyPolicy,name='privacyPolicy'),
]
