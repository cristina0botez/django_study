from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.db import models


__all__ = ['Publisher', 'Author', 'Book', 'UserAuthorInterest']


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


class UserAuthorInterest(models.Model):
    user = models.ForeignKey(get_user_model())
    author = models.ForeignKey(Author)
    accessed = models.IntegerField(default=0)

    class Meta:
        app_label = 'experiments'
        unique_together = ('user', 'author')

    @classmethod
    def get_interest_of_user_in_author(cls, user, author):
        try:
            uai = cls.objects.get(user=user, author=author)
        except cls.DoesNotExist:
            return None
        else:
            return uai.accessed

    @classmethod
    def increment_interest_of_user_in_author(cls, user, author):
        try:
            uai = cls.objects.get(user=user, author=author)
        except cls.DoesNotExist:
            uai = cls.objects.create(user=user, author=author, accessed=1)
        else:
            uai.accessed += 1
            uai.save()
        return uai.accessed