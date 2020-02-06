from django.contrib import admin
from staff.models import StaffProfile, StaffReport

@admin.register(StaffProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','first_name', 'last_name', 'surname', 'staff_id']
    link_display = ['staff_id']


@admin.register(StaffReport)
class ReportAdmin(admin.ModelAdmin):
    list_display = ["user", "staf", "message"]
    link_display = ['user']

