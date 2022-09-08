from django.db import models


class Continent(models.Model):

    class Meta:
        verbose_name_plural = 'Continents'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Adventure(models.Model):

    continent = models.ForeignKey('Continent', null=True, blank=True,
                                  on_delete=models.SET_NULL)
    country = models.ForeignKey('Country', null=True, blank=True,
                                on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    theme = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Excursion(models.Model):

    country = models.ForeignKey('Country', null=True, blank=True,
                                on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
