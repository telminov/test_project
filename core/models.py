from django.db import models


class Book(models.Model):
    name = models.CharField('Название', max_length=255)
    pages = models.IntegerField('Количество страниц', null=True, blank=True)

    def __str__(self):
        return self.name
