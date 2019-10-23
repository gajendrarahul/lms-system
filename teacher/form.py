from django import forms
from . models import Teacher
class AddteacherForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Teacher
        exclude = ['user']

class TeacherEditForm(forms.ModelForm):
    fullname =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Teacher
        fields =['fullname','address']