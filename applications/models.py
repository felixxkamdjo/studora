from django.db import models
from django.conf import settings
from projects.models import Project


class Application(models.Model):

    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('rejected', 'Refusée'),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications',
        verbose_name='Étudiant',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='applications',
        verbose_name='Projet',
    )
    motivation = models.TextField(verbose_name='Lettre de motivation')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Statut',
    )
    applied_at = models.DateTimeField(auto_now_add=True, verbose_name='Postulé le')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modifié le')

    class Meta:
        verbose_name = 'Candidature'
        verbose_name_plural = 'Candidatures'
        ordering = ['-applied_at']
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'project'],
                name='unique_application_per_student_project'
            )
        ]

    def __str__(self):
        return f"{self.student.get_full_name()} → {self.project.title}"

    @property
    def is_pending(self):
        return self.status == 'pending'

    @property
    def is_accepted(self):
        return self.status == 'accepted'