from django.db import models
from django.urls import reverse

# Create your models here.
class WaterBody(models.Model):
    salinity_choices =(
        ('Fr', 'Fresh Water'),
        ('Sa', 'Salt Water'),
        ('Br', 'Brackish (Mix of Salt and Fresh Water)')
    )

    name = models.CharField(max_length=100, null= True)
    salinity = models.CharField(
        max_length=2,
        choices=salinity_choices,
        default = salinity_choices[1][0],
    )

    def __str__(self):
        return f"{self.name} is a {self.get_salinity_display()} body of water"

        
class Shark(models.Model):
    species = models.CharField(max_length=100)
    image = models.URLField(max_length=500)
    length = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    top_speed = models.CharField(max_length=100)
    preferred_prey = models.CharField(max_length=100)
    water_bodies = models.ManyToManyField(WaterBody)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse("detail", kwargs={"shark_id": self.id})


class Coast(models.Model):
    name = models.CharField(max_length=100, null= True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    water_body = models.ForeignKey(WaterBody, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} coast is in {self.city}, {self.country}"