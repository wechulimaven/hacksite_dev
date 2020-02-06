from django.urls import path
from . import views
app_name = 'QR'
urlpatterns = [
    path('', views.hacker_view, name = 'hacker'),
    path('hack/', views.myview, name = 'hackqr'),
]