from django.db import models
from django.core import validators


# Create your models here.
class Category(models.Model):
    NANE_MAX_LEN = 15
    name = models.CharField(max_length=NANE_MAX_LEN,)


class Product(models.Model):
    NANE_MAX_LEN = 25
    PRICE_MIN_VALUE = 0.00

    name = models.CharField(max_length=NANE_MAX_LEN, )

    price = models.FloatField(validators=(validators.MinValueValidator(PRICE_MIN_VALUE),))

    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
