from django import forms
#Bieu mau tạo(signup) user(UserCreationForm), biểu mẫu login(AuthenticationForm) 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# import db models
from django.contrib.auth.models import User

#có viết if pass=pass(db) trong authen luôn 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        #User den tu Django
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email address',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))




