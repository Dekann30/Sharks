from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Sighting(models.Model):
    shark_species = models.CharField(max_length=100)
    beach_name = models.CharField(max_length=100, null= True)
    city_state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    comment = models.TextField()

    def __str__(self):
        return self.beach_name

    def get_absolute_url(self):
        return reverse("sightings_detail", kwargs={"pk": self.id})


class Shark(models.Model):
    species = models.CharField(max_length=100)
    image = models.URLField(max_length=500)
    length = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    top_speed = models.CharField(max_length=100)
    preferred_prey = models.CharField(max_length=100)
    sightings = models.ManyToManyField(Sighting)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse("detail", kwargs={"shark_id": self.id})




