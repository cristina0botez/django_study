from django.db import models


class Flavor(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    scoops_remaining = models.BigIntegerField(default=0)

    def __unicode__(self):
        return self.name


class IceCreamStore(models.Model):

    name = models.CharField(max_length=100)
    block_address = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
