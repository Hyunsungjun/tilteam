from django.db import models
from core import models as core_models


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """
    
    name = models.CharField(max_lenght=140)
    description = models.TextField()
    country = 