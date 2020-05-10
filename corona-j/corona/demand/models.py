from django.db import models

# Create your models here.
class Services(models.Model):
    commodity = models.CharField(max_length = 200, null = True)
    location = models.CharField(max_length = 200, null = True)
    order = models.IntegerField(max_length = 1000, null = True)
    date_created = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return self.location

class Service(models.Model):
    commodity = models.CharField(max_length = 200, null = True)
    location = models.CharField(max_length = 200, null = True)
    order = models.IntegerField(max_length = 1000, null = True)
    date_created = models.DateTimeField(auto_now_add = True)

'''class Customer(models.Model):
    STATUS = (
            ('Available','N/A'),
    )
#for secretary of the society'''