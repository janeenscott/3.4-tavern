from django.db import models


class Lunch(models.Model):

    nickname = models.CharField(max_length=50)
    user = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.nickname

class Location(models.Model):
    lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE)
    votes = models.IntegerField()


    def __str__(self):
        return self.lunch