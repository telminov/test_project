from django.db import models


class Author(models.Model):
    name = models.CharField('Имя', max_length=255, unique=True)
    birth = models.DateField('Год рождения', null=True, blank=True)


class Book(models.Model):
    authors = models.ManyToManyField(Author,
                                     null=True, blank=True, related_name='books')
    name = models.CharField('Название', max_length=255)
    pages = models.IntegerField('Количество страниц', null=True, blank=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

