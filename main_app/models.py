from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExtendedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    profilepic = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} extended information'

class DisplayType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Timeline(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    primary = models.BooleanField(default=False)
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    displaytype = models.ForeignKey(DisplayType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    datetime = models.DateTimeField()
    summary = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.title

