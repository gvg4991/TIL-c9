from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm): #UserChangeForm을 전부 다 쓰지않고 폼의 몇가지만 쓰겠다.
    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name',]