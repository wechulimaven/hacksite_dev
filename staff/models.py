from django.db import models
from django.contrib.auth.models import User
from examcard.models import Unit, Log, Report

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    staff_id = models.CharField(max_length=62, )
    first_name = models.CharField(max_length=62, )
    last_name = models.CharField(max_length=62, )
    surname = models.CharField(max_length=62, )
    profile_photo = models.ImageField(upload_to='Staff_profile')
    timestamp = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        """Unicode representation of Report."""
        return f'{self.user} {self.staff_id} {self.first_name} {self.first_last_name}'
    
class StaffReport(models.Model):
    user = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    staf = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now = True)
    

    class Meta:
        """Meta definition for Report."""

        verbose_name = 'StaffReport'
        verbose_name_plural = 'StaffReports'

    def __str__(self):
        """Unicode representation of Report."""
        return f'{self.user} {self.staff} {self.message}'
