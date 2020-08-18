from django.db import models

# Create your models here.
class Movie(models.Model):
    """Django Model class representing a movie

    Attributes:
        title (str): Title of a movie
        length (int): Length of a movie in minutes.
        release_year(int): Year movie was released.
    """
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

class Customer(models.Model):
    """Django Model class representing a customer

    Attributes:
        first_name (str): Customer's first name.
        last_name (str): Customer's last name.
        phone (int): Customer's phone number.
    """
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()