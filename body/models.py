from django.db import models
from datetime import datetime

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(default=datetime.now)
    image = models.CharField(max_length=500, blank=True)
    blog1 = models.TextField(blank=True)
    image2 = models.CharField(max_length=500, blank=True)
    blog2 = models.TextField(blank=True)
    image3 = models.CharField(max_length=500, blank=True)
    blog3 = models.TextField(blank=True)
    image4 = models.CharField(max_length=500, blank=True)
    blogl = models.TextField(blank=True)

    def summary(self):
        return self.blog1[0:250] + '.....'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date',]

class project(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.now)
    icon = models.CharField(max_length=500, blank=True)
    short_desc = models.CharField(max_length=250)
    description = models.TextField()
    ss1 = models.CharField(max_length=500, blank=True)
    ss2 = models.CharField(max_length=500, blank=True)
    ss3 = models.CharField(max_length=500, blank=True)
    ss4 = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date',]
