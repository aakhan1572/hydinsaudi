import os
from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from sorl.thumbnail import get_thumbnail
from django.dispatch import receiver

from phonenumber_field.modelfields import PhoneNumberField
#from django.db.models.signals import post_delete
#from accounts.utils import file_cleanup

class Countrycode(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
         return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
         return self.name


class CityCode(models.Model):
    name = models.CharField(max_length=128)
    countrycode = models.ForeignKey(Countrycode, on_delete=models.CASCADE, related_name='countrycode')

    def __str__(self):
         return self.name


class LocationCode(models.Model):
    name = models.CharField(max_length=128)
    locationcode = models.ForeignKey(CityCode, on_delete=models.CASCADE, related_name='locationcode')

    def __str__(self):
         return self.name


class SubLocationCode(models.Model):
    name = models.CharField(max_length=128)
    sublocationCode = models.ForeignKey(LocationCode, on_delete=models.CASCADE, related_name='sublocationCode')

    def __str__(self):
         return self.name


class Category(models.Model):
    name = models.CharField(max_length = 150 , null = False)
    slug = models.CharField(max_length = 150 , null = False , unique = True)
    thumbnail = models.ImageField(upload_to='users/thumnail', blank=True, null=True)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def clean(self):
        self.category_name = self.name.capitalize()

    def get_url(self):
        return reverse('expads_by_category', args=[self.slug])

    class Meta:
        ordering = ('-created','-updated')
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

class Expatad(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,  on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    countrycode = models.ForeignKey(Countrycode ,default='Saudi Arabia',  on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose , on_delete=models.CASCADE)
    citycode = models.ForeignKey(CityCode ,  default='Jeddah',on_delete=models.CASCADE)
    locationcode =models.CharField(max_length=200)
    sublocationcode = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    area = models.CharField(max_length=100,default=100)
    areameasurement = models.CharField(max_length=40,default='Square Feet')
    contactno = PhoneNumberField()
    zipcode = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    Description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created','-updated')
        verbose_name = 'expatad'
        verbose_name_plural = 'expatads'

    def __str__(self):
        return self.fullname


class ExpatImage(models.Model):
    expatads = models.ForeignKey(Expatad, on_delete=models.CASCADE,related_name='expatads')
    images = models.FileField(upload_to='users/images', blank=True, null=True)

    @property
    def thumbnail(self):
        if self.images:
            return get_thumbnail(self.images, '50x50', quality=90)
        return None

    def delete(self):
        self.images.delete()
        super().delete()            
    
    def __str__(self):
        return self.expatads.contactno

class Contactme(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    contactno = PhoneNumberField()
    email = models.CharField(max_length=150)
    Description = models.CharField(max_length=500)
    is_fallowed = models.CharField(max_length=100,default="Yet Not Followed This Message")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

class Interested(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    contactno = PhoneNumberField()
    email = models.CharField(max_length=150)
    Description = models.CharField(max_length=500)
    is_fallowed = models.CharField(max_length=100,default="Yet Not Followed This Message")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname



def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(models.signals.post_delete, sender=ExpatImage)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.images:
        _delete_file(instance.images.path)       

@receiver(models.signals.post_delete, sender=Expatad)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes thumbnail files on `post_delete` """
    if instance.cover_photo:
        _delete_file(instance.cover_photo.path)