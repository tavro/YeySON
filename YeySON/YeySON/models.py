from django.db import models


class Committee(models.Model):
    title = models.CharField(max_length=128)


class Contact(models.Model):
    committee = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    mail = models.CharField(max_length=128)


class Post(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField()
    content = models.TextField(max_length=4096)


class Page(models.Model):
    title = models.CharField(max_length=128)
    path = models.CharField(max_length=64)
    content = models.TextField(max_length=4096)