from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    ROLE_CHOICES = [
        ('student', 'Étudiant'),
        ('teacher', 'Enseignant'),
        ('admin', 'Administrateur'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student',
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    @property
    def is_student(self):
        return self.role == 'student'

    @property
    def is_teacher(self):
        return self.role == 'teacher'

    @property
    def is_admin(self):
        return self.role == 'admin'