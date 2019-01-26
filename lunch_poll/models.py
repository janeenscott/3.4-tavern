from django.db import models


class Lunch(models.Model):

    nickname = models.CharField(max_length=50)
    user = models.CharField(max_length=100)
    date = models.DateField()


class Location(models.Model):
    lunch = models.ForeignKey(to Lunch)
