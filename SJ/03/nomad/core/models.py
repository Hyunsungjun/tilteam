from django.db import models

class TimeStampedModel(models.Model):

    """ Room Model Definition """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True