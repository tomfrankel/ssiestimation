from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Size(models.Model):
    size=models.CharField(max_length=200,null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.size)


class Material(models.Model):
    material=models.CharField(max_length=200,null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.material)

class Piping(models.Model):
    piping=models.CharField(max_length=200,null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.piping)

class Price(models.Model):
    size = models.ForeignKey(Size, null=True, blank=True)
    material = models.ForeignKey(Material, null=True, blank=True)
    piping = models.ForeignKey(Piping, null=True, blank=True)
    pipes_price = models.DecimalField(max_digits=8, decimal_places=2,default=0, null=True, blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.pipes_price)


# class Pipes(models.Model):
#     name = models.CharField(max_length=100,null=True,blank=True)
#     active = models.BooleanField(default=True)
#     added_on = models.DateTimeField(auto_now_add=True, db_index=True)
#     updated_on = models.DateTimeField(null=True, blank=True, db_index=True)
#
#     def __str__(self):
#         return u'{0}'.format(self.name)

class Accessories(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    # pipe_type = models.ForeignKey(Pipes, null=True,blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.name)


class AccessoriesSize(models.Model):
    accessories = models.ForeignKey(Accessories, null=True,blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.size)


class AccessoriesType(models.Model):
    accessories = models.ForeignKey(Accessories, null=True,blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.type)


class AccessoriesPrice(models.Model):
    name = models.ForeignKey(Accessories, null=True, blank=True)
    size = models.ForeignKey(AccessoriesSize, null=True, blank=True)
    type = models.ForeignKey(AccessoriesType, null=True, blank=True)
    accessories_price = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return u'{0}'.format(self.accessories_price)




class TotalCost(models.Model):
    description = models.CharField(max_length=800, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2,default=0, null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2,default=0, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(null=True, blank=True, db_index=True)




