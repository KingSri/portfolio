from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description= models.TextField()
    date = models.DateField()
    url = models.URLField()
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
