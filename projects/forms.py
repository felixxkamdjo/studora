from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'domain',
            'max_students',
            'status',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Titre du projet',
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Décrivez le projet en détail...',
            }),
        }
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'domain': 'Domaine',
            'max_students': "Nombre max d'étudiants",
            'status': 'Statut',
        }