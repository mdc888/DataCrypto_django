from django.db import models


class Data_crypto(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(default="developers.jpg",blank=True)
    def __str__(self):
        return self.title


