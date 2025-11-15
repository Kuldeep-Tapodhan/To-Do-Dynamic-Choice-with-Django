from django.db import models

# Create your models here.

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

    def __str__(self):
        return self.title