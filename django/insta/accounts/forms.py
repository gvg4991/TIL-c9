from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm): #UserChangeForm을 전부 다 쓰지않고 폼의 몇가지만 쓰겠다.
    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name',]
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','introduction','image',]