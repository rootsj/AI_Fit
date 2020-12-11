from django import forms
from datetime import datetime


class LoginForm(forms.Form):
    email = forms.CharField(label='Your Email', max_length=255)
    password = forms.CharField(label='Your Password', max_length=30, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    email = forms.CharField(label='* Email', max_length=255)
    password = forms.CharField(label='* Password', max_length=30, widget=forms.PasswordInput)
    nick_name = forms.CharField(label="* 닉네임", max_length=10)
    date_of_birth = forms.DateField(label="* 생년월일", initial="2000-01-01", widget=forms.SelectDateWidget(years=range(1900, datetime.today().year + 1)))
    #profile_img = forms.FileField(label='프로필 사진', required=False)
    