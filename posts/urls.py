# urls.py
from django.urls import path
from accounts import views

urlpatterns = [
    path('<slug:post_slug>/', views.OnePost, name='post_detail'),
    
]
