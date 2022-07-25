from tkinter import image_types
from turtle import title
from embed_video.fields import EmbedVideoField
from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    url = EmbedVideoField()

    def __str__(self):
        return self.title


class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    image = models.FileField()

    def __str__ (self):
        return self.name
