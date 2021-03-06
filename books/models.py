from django.db import models

# Create your models here.
class Book(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()

    class Meta:
        ordering = ['published']
