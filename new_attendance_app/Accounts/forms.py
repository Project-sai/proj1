from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email','phone_number')