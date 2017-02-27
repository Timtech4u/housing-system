from django.db import models


class House(models.Model):
    HOUSE_STATUS = (
        ('ALA', 'ALLOCATED'),
        ('DEA', 'UNALLOCATED'),
        ('WAI', 'WAITING'),
	)
    status = models.CharField(max_length=3, choices=HOUSE_STATUS, default='WAI')
    house_code = models.CharField(max_length=50)
    house_type = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    no_of_rooms = models.IntegerField()
    year_of_lease = models.IntegerField()
    
    def __str__(self):
        return self.house_code


class Occupant(models.Model):
    house = models.OneToOneField(House, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    num_of_kids = models.IntegerField(blank=True, null=True)
    tel_number = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return "{} {} ".format(self.first_name, self.second_name)

