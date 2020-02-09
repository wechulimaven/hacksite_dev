from django import forms
from .models import StaffProfile, StaffReport
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, get_user_model, login, logout


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
        
class StaffLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password', 'placeholder':'Password','required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(StaffLoginForm, self).clean(*args, **kwargs)

                       


