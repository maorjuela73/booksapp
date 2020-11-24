from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=50, default='No me acuerdo')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='Libro muy interesante')

    def __str__(self):
        return self.name
