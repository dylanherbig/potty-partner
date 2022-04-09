from pydoc import describe
from re import T
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


import datetime

# Create your models here.

class Feature(models.Model):
    title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title 

class Toilet(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    title = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    feature = models.ManyToManyField(Feature, related_name='features', blank=True, null=True)

    def __str__(self):
        return self.title        

class ToiletReview(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, blank=False, null=True)
    toilet = models.ForeignKey(Toilet, related_name='reviews', on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=175, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]        
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now    
    
    def __str__(self):
        return self.title    
