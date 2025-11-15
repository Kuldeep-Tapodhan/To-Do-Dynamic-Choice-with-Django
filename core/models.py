from django.db import models
from django.contrib.auth.models import User # Import the User model

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    
    status = models.ForeignKey(
        Status, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='tasks'
    )
    
    # --- This is the new, correct line ---
    # We add null=True and blank=True so existing tasks don't break
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="tasks",
        null=True, # Allow existing tasks to have a null user
        blank=True
    )

    def __str__(self):
        return self.title