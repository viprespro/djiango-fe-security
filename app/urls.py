from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('xss/', views.xss, name='xss'),
    path('comments/', views.comments, name='comments')
]
