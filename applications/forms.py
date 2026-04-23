from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['motivation']
        widgets = {
            'motivation': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Expliquez pourquoi vous souhaitez travailler sur ce projet, vos compétences pertinentes, et ce que vous espérez apprendre...',
            }),
        }
        labels = {
            'motivation': 'Lettre de motivation',
        }