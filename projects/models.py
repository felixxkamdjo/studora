from django.db import models
from django.conf import settings


class Project(models.Model):

    STATUS_CHOICES = [
        ('open', 'Ouvert'),
        ('closed', 'Fermé'),
        ('completed', 'Terminé'),
    ]

    DOMAIN_CHOICES = [
        ('informatique', 'Informatique'),
        ('mathematiques', 'Mathématiques'),
        ('physique', 'Physique'),
        ('chimie', 'Chimie'),
        ('biologie', 'Biologie'),
        ('economie', 'Économie'),
        ('autre', 'Autre'),
    ]

    title = models.CharField(max_length=200, verbose_name='Titre')
    description = models.TextField(verbose_name='Description')
    domain = models.CharField(
        max_length=50,
        choices=DOMAIN_CHOICES,
        default='informatique',
        verbose_name='Domaine',
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name='Enseignant',
    )
    max_students = models.PositiveIntegerField(
        default=1,
        verbose_name='Nombre max d\'étudiants',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open',
        verbose_name='Statut',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Créé le')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modifié le')

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def accepted_count(self):
        return self.applications.filter(status='accepted').count()

    @property
    def is_full(self):
        return self.accepted_count >= self.max_students

    @property
    def is_open(self):
        return self.status == 'open'