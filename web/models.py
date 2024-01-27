from django.db import models

# Create your models here.

class Facilities(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)

class School(models.Model):
    image = models.ImageField(upload_to='media/school')
    name = models.CharField(max_length=100)
    Timage = models.ImageField(upload_to='media/Teachers')
    Tname = models.CharField(max_length=150)
    Coursefee = models.IntegerField()
    age = models.CharField(max_length=50)
    Time = models.CharField(max_length=50)
    Capacity = models.IntegerField()

class Teachers(models.Model):
        image = models.ImageField(upload_to='media/teachers')
        name = models.CharField(max_length=100)
        designation = models.CharField(max_length=250)

class Clients(models.Model):
        content = models.CharField(max_length=500)
        image = models.ImageField(upload_to='media/clients')
        name = models.CharField(max_length=100)
        profession = models.CharField(max_length=100)


class Contact(models.Model):
        guardian_name = models.CharField(max_length=100)
        guardian_email =  models.CharField(max_length=100)
        child_name = models.CharField(max_length=100)
        child_age = models.IntegerField()
        message = models.CharField(max_length=300)
   
   
   
   
        def __str__(self):
            return self.name
    