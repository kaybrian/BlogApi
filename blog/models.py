from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=250)
    description = models.TextField(max_length=340)
    date_Created = models.DateField(auto_now_add=True)
    date_Updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title