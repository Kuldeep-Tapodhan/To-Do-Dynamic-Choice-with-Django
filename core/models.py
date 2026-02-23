from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class TimeStampedModel(models.Model):
    """Abstract base model that provides created_at and modified_at fields."""
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, TimeStampedModel):
    """Custom User model with additional profile fields."""
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    bio = models.TextField(max_length=500, blank=True, default='')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']

    def __str__(self):
        return self.username


class Status(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ['id']

    def __str__(self):
        return self.name


class Task(TimeStampedModel):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title