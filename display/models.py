from django.db import models


class SampleModel(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=20)
