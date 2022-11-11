from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home_Page.as_view(), name='home'),
]
