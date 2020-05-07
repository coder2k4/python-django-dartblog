from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    """ Abstract model for time stamps """

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата Обновления')

    class Meta:
        abstract = True
