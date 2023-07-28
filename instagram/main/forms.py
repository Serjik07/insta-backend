from django.forms import ModelForm, EmailInput,PasswordInput
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ["login","password"]

        widgets = {
            "login" : EmailInput(attrs={
                'placeholder': 'Телефон, имя пользователя или эл. адрес',
                'autocomplete': 'off'
            }),
            "password" : PasswordInput(attrs={
                'placeholder': 'Пароль'
            }),
        }
