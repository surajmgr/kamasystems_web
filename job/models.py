from django.db import models
from datetime import datetime

# Create your models here.

class topProjects(models.Model):
    icon = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    site = models.URLField(max_length=300)

class featurette(models.Model):
    #featurete 1
    f1_title = models.CharField(max_length=200, blank=True)
    f1_stxt = models.CharField(max_length=300, blank=True)
    f1_desc = models.TextField(blank=True)
    f1_img = models.CharField(max_length=500, blank=True)

    #featurete 2
    f2_title = models.CharField(max_length=200, blank=True)
    f2_stxt = models.CharField(max_length=300, blank=True)
    f2_desc = models.TextField(blank=True)
    f2_img = models.CharField(max_length=500, blank=True)

    #featurete 3
    f3_title = models.CharField(max_length=200, blank=True)
    f3_stxt = models.CharField(max_length=300, blank=True)
    f3_desc = models.TextField(blank=True)
    f3_img = models.CharField(max_length=500, blank=True)

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField(default=datetime.now)
    message = models.CharField(
        max_length=2000,
        help_text='Write your message here...'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-date',]
