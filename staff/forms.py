from django import forms
from .models import StaffProfile, StaffReport
from django.contrib.auth.forms import UserChangeForm


class StaffProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'first_name', 'required': 'true'}))
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'sirname', 'required': 'true'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'last_name', 'required': 'true'}))
    staff_id = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'adm_number', 'required': 'true'}))
    profile_photo = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone','id': 'profile_photo', 'accept':'image/*', 'required': 'true'}))
    
    class Meta:
        model = StaffProfile
        fields = ['first_name','last_name','surname','profile_photo']
        
class StaffEditProfileForm(UserChangeForm):
    class Meta:
        model = StaffProfile
        fields = ['first_name','last_name','surname','staff_id','profile_photo']
                       


