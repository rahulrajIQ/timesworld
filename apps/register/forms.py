from django import forms
from .models import User
from django.core.exceptions import ValidationError


def mobile_validator(value):
        if len(str(value)) !=10:
            raise ValidationError(
            "Mobile no. should be of 10 Digits."
        )

def name_validator(value):
    if not value.replace(' ','').isalpha():
            raise ValidationError(
            "Name can only contain Alphabets."
        )
    
def password_validator(value):
    if len(str(value)) >=10:
            raise ValidationError(
            "Password is too short! Minimum 6 characters required."
        )


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length = 255,validators=[name_validator])
    email = forms.EmailField(max_length=255)
    country = forms.CharField(max_length=255)
    mobile = forms.IntegerField(validators=[mobile_validator])
    nationality = forms.CharField(max_length = 255) 

    # ROLES = (

    #     ('student', 'student'),
    #     ('staff', 'staff'),
    #     ('admin', 'admin'),
    #     ('editor', 'editor')

    # )

    # role = forms.ChoiceField(choices = ROLES)

    password = forms.CharField(widget=forms.PasswordInput,validators=[password_validator])
    confirm_password = forms.CharField(widget=forms.PasswordInput,validators=[password_validator])

    class Meta:
        model = User
        fields = '__all__'
        