from django.db import models


class Table(models.Model):

    name = models.TextField()
    width = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.number} - {self.name}'


class Path(models.Model):

    path = models.TextField()

    def __str__(self):
        return self.path
