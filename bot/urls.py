from django.urls import path

from . import views

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('hello/', views.index),
    path('webhook/', views.webhook_message),
]