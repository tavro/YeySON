from django.db import models

class Committee(models.Model):
    title = models.CharField(max_length=128)

class Contact(models.Model):
    committee = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    mail = models.CharField(max_length=128)