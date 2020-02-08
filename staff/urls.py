from django.urls import path
from . import views


app_name = 'staff'
urlpatterns = [
    path('',views.staff_dashboard, name='staff_dashboard'),
    path('attendance/', views.attendance_reg, name='attendance'),
    path('scanner/',views.exam_card_scanner, name='scan'),
    path('create_profile/', views.staff_create_profile, name='create_profile'),
    path('stafprofile/', views.staffprofile, name='stafprofile'),
    path('staflogin/', views.stafflogin, name = 'staflogin'),
    
    
    
]
