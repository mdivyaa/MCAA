from django import forms
from .models import FacultyModel

class FacultyForm(forms.ModelForm):
    class Meta:
        model = FacultyModel
        fields = ['name', 'email', 'department']