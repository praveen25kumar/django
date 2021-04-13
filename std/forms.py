from django import forms

from .models import student


class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','email','password','mobile']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','max_length':10}),



        }