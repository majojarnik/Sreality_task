from django.db import models

# Create your models here.


class Flat(models.Model):
    title = models.CharField()
    image_url = models.CharField()
