from django import forms
from college.models import Employee, Student,Employee1
from django.core.exceptions import ValidationError

from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)
import os
class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee1
        fields = ['name', 'email', 'address']


class ChangePasword(forms.Form):

    old_password = forms.CharField(max_length=50)
    new_password = forms.CharField(max_length=50)
    repeat_password = forms.CharField(max_length=50)


class MyForm(forms.Form):

    username = forms.CharField(label="NAME",max_length=50)
    email = forms.CharField()
    address = forms.CharField(max_length=255)


class ProfileForn(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=50)

def validateExt(value):

    logger.error(os.path.splitext(value.name))
    ext =os.path.splitext(value.name)[1]
    extList = ['.png']
    if ext.lower() not in extList:
        raise ValidationError("File extestions must be .png!")


class EmpForm(forms.ModelForm):

    #email = forms.EmailField()
    picture = forms.FileField(validators=[validateExt])

    class Meta:

        model = Employee

        fields = ['username', 'email', 'address', 'city','picture']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class UniqueUserEmailField(forms.EmailField):

    def validate(self, value):
        super(forms.EmailField, self).validate(value)
        try:
            User.objects.get(email = value)
            raise forms.ValidationError("Email already exist!")
        except User.MultipleObjectsReturned:
            raise forms.ValidationError("Email already exist!")
        except User.DoesNotExist:
            pass


def validateEmail(value):
    try:
        User.objects.get(email=value)
        raise ValidationError("Email already exist!")
    except User.MultipleObjectsReturned:
        raise ValidationError("Email already exist!")
    except User.DoesNotExist:
        pass


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Email address', validators=[validateEmail])


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = ['name', 'email', 'emp_id']

