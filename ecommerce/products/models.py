from django.db import models
from django.dispatch import receiver

from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.urls import reverse
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


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def features(self):
        return self.get_queryset().featured()

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


# Create your models here.
class Product(models.Model):
    objects = ProductManager()
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=30)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=False)
    featured = models.BooleanField(default=False)  # +active
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse('products:detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
