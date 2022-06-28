from django.db import models

# Create your models here.
# 2) create a model (db table & its attrs - then migrate to db)
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)


    # The __str__ method just tells Django what to print when it needs to print out an instance of the Hero model.
    def __str__(self):
        return self.name


class Villian(models.Model):
    name = models.CharField(max_length=60)
    powerlevel = models.CharField(max_length=1)


    def __str__(self):
        return self.name
