from django.urls import path
from . import views



app_name = 'examcard'
urlpatterns = [
    path('', views.home_dashboard, name = 'home_dashboard'),
    path('register/', views.student_register, name = 'student_register'),
    path('login/', views.student_login, name = 'login'),
    path('create/', views.student_create_profile, name = 'student_create_profile'),
    path('unit/', views.add_unit, name = 'unit'),
    path('card/', views.exam_card, name = 'exam_card'),
    path('scan/', views.exam_card_scanner, name = 'scan'),
    path('loglist/', views.log_list, name = 'log_list'),
    path('report/', views.report_list, name = 'report_list'),
    path('report/<int:id>/', views.make_report, name = 'make_report'),
    path('logout/', views.user_log_out, name = 'user_log_out'),
    path('profile/', views.profile, name = 'profile'),
]

