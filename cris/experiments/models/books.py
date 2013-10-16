from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models


__all__ = ['Publisher', 'Author', 'Book']


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]
        app_label = 'experiments'


    def __unicode__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots',
                                 null=True, blank=True)
    last_accessed = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(get_user_model(), null=True, blank=True)

    class Meta:
        app_label = 'experiments'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'author_id': self.pk})


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    class Meta:
        app_label = 'experiments'
