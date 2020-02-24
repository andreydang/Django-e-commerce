from django.db import models
import random
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9999999)
    name, ext = get_filename_ext(filename)
    final_filename = '{}{}'.format(new_filename, ext)
    return "products/{}/{}".format(new_filename, final_filename)


class ProductManager(models.Manager):

    def get_by_id(self, id):
        return self.get_queryset().filter(id=id)


# Create your models here.
class Product(models.Model):
    objects = ProductManager()
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=30)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
