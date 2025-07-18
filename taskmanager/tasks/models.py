from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title 
     