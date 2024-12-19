from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Sneakers(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "so'm"
    RU = "₽"
    ENG = "$"
    the_price =(
        (UZ, "so'm"),
        (RU, "₽"),
        (ENG, "$")
    )
    price_type = models.CharField(max_length=10,
                                  choices=the_price,
                                  default="so'm")
    price = models.IntegerField()
    image = models.ImageField()

