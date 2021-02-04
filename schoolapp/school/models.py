from django.db import models


# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    group = models.CharField(max_length=50)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=50)
    visible = models.BooleanField(default=False)
