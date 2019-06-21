from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Size(models.Model):
    size=models.CharField(max_length=200,null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)


class Material(models.Model):
    material=models.CharField(max_length=200,null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

class Piping(models.Model):
    piping=models.CharField(max_length=200,null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

class Accessories(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

class Accessories_size(models.Model):
    accessories = models.ForeignKey(Accessories, null=True,blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)
