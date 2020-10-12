from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(primary_key = True, max_length = 100)
    image = models.ImageField(upload_to = 'visuals/assets')

    def __str__(self):
        return self.name
