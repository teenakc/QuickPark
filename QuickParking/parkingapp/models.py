from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class ParkingArea(models.Model):
    parkingname = models.CharField(max_length=122)
    location = models.CharField(max_length=122)
    phoneno = models.CharField(max_length=122)
    space = models.CharField(max_length=20)

    def __str__(self):
        return self.parkingname
    


class UserReservation(models.Model):
    username = models.CharField(max_length=122)
    userno = models.CharField(max_length=12)
    vehicalno = models.CharField(max_length=30)
    vehicaltype = models.CharField(max_length=10)

    def __str__(self):
        return self.vehicalno+self.username
    
