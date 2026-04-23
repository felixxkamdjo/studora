from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=50,
        label='Prénom',
        widget=forms.TextInput(attrs={'placeholder': 'Votre prénom'}),
    )
    last_name = forms.CharField(
        max_length=50,
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Votre nom'}),
    )
    email = forms.EmailField(
        label='Adresse email',
        widget=forms.EmailInput(attrs={'placeholder': 'votre@email.com'}),
    )
    role = forms.ChoiceField(
        choices=[
            ('student', 'Étudiant'),
            ('teacher', 'Enseignant'),
        ],
        label='Rôle',
        widget=forms.Select(),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'role',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label='Adresse email',
        widget=forms.EmailInput(attrs={'placeholder': 'votre@email.com'}),
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
    )