from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

# from django import forms
# from django.contrib.auth.models import User
# from basic_app.models import UserProfileInfo
#
#
# class UserForm(forms.ModelForm):
#     """docstring for UserForm."""
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model = User
#         fields = ('username','email','password')
#
# class UserProfileInfoForm(forms.ModelForm):
#     """docstring for UserForm."""
#
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portifolio_site','profile_pic')
