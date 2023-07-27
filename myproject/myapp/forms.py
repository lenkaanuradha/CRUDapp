from django import forms
from .models import Student
from django import forms
class Studentform(forms.ModelForm):
  class Meta:
     model = Student
     fields=['Name','Email','password']
     widgets={
        'password':forms.PasswordInput(attrs={'class':'form-control'}),
        'Name':forms.TextInput(attrs={'class':'form-control'}),
        'Email':forms.EmailInput(attrs={'class':'form-control'})
        }