from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    premier_date = models.DateField()
    genres = models.ManyToManyField('movies.Genre', related_name='movies')
    description = models.TextField()
    poster = models.ImageField(upload_to='posters')
    directors = models.ManyToManyField('movies.Person', related_name='directed')
    writers = models.ManyToManyField('movies.Person', related_name='wrote')
    actors = models.ManyToManyField('movies.Person', related_name='acted_in')
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # 10.0 / 9.9 / 99.9
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    # directed
    # wrote
    # acted_in

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return self.name

