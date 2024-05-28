from django import forms

class StudentForm(forms.Form):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=25)
    last_name=forms.CharField(max_length=25)
    age=forms.IntegerField(max_value=100)