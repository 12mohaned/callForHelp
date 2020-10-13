from django.db import models

class CountryManager(models.Manager):
    def edit_country_name(self, pre_name, curr_name):
        country = Country.objects.get(name = pre_name)
        country.name = curr_name
        country.save()
        previous_country = Country.objects.get(name = pre_name)
        previous_country.delete()
        return country

    def create_country(self, name, image):
        country = self.create(name = name, image = image)
        return country

class Country(models.Model):
    name = models.CharField(primary_key = True, max_length = 100)
    image = models.ImageField(upload_to = 'visuals/assets')
    objects = CountryManager()
    def __str__(self):
        return self.name
