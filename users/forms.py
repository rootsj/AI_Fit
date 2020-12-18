from django import forms
from datetime import datetime


class LoginForm(forms.Form):
    email = forms.CharField(label='Your Email', max_length=255)
    password = forms.CharField(label='Your Password', max_length=30, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    email = forms.CharField(label='* Email', max_length=255, widget=forms.EmailInput)
    password1 = forms.CharField(label='* Password', min_length=6, max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label='* Password 확인', min_length=6, max_length=30, widget=forms.PasswordInput)
    nick_name = forms.CharField(label="* 닉네임", max_length=10)
    date_of_birth = forms.DateField(label="* 생년월일", initial="2000-01-01", widget=forms.SelectDateWidget(years=range(1900, datetime.today().year + 1)))


class EditForm(forms.Form):
    current_password = forms.CharField(label='* 현재 Password', max_length=30, widget=forms.PasswordInput)
    password1 = forms.CharField(label='* Password', min_length=6, max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label='* Password 확인', min_length=6, max_length=30, widget=forms.PasswordInput)


class ChangePwForm(forms.Form):
    password1 = forms.CharField(label='Password', min_length=6, max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password 확인', min_length=6, max_length=30, widget=forms.PasswordInput)
