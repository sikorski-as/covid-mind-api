from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name} ({self.color})'


class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
    link = models.URLField()
    visible = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f'{self.title} ({self.date})'
