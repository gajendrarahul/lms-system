from django import forms
from manager . models import Announcement
from django.forms.widgets import Textarea
class AnnouncementContentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Announcement
        fields = ['description']