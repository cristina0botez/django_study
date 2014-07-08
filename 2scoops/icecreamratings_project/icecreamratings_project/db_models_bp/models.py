from django.db import models


class AnotherManager(models.Manager):

    def get_query_set(self):
        result = super(AnotherManager, self).get_query_set().filter(
            some_field__lt=100).order_by('some_field')
        return result


class Parent(models.Model):

    some_field = models.IntegerField(null=True)

    the_enemy = AnotherManager()

    def __unicode__(self):
        return u'Parent #%s' % self.some_field


class ParentSubclasser(Parent):

    reason = models.TextField(null=True)

    another_mngr = AnotherManager()


class Tutor(Parent):
    minimals = AnotherManager()

    class Meta:
        proxy = True

    def __unicode__(self):
        return u'Tutor #%s' % self.some_field
