from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
