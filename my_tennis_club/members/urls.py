from django.urls import path
from members import views

urlpatterns = [
    path('', views.members, name='members'),
]
