from django.db import models

class locomotivrecord(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Create your models here.
