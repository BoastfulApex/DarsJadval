from django import forms
from .models import *


class TeacherForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ))

    zoom_link = forms.URLField(
        label="Zoom Link",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ))

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ))

    class Meta:
        model = Teacher
        fields = ['name', 'zoom_link', 'description']


class TeacherFileForm(forms.Form):
    file = forms.FileField(
      widget=forms.FileInput()
    )


class StudyGroupForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ))

    weekly_schedule = forms.ImageField(
      widget=forms.FileInput()
    )

    class Meta:
        model = StudyGroup
        fields = ['name', 'weekly_schedule']
