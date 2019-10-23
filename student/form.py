from django import forms
from . models import Student
class AddstudentForm(forms.ModelForm):
    fullname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    enrolled_course = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Student
        exclude = ['user']

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =['fullname','address']