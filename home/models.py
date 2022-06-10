from django.db import models

# Create your models here.

class People(models.Model):
    fname = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField() 
    
    def __str__(self):
        return self.fname 

class Address(models.Model):
    people = models.ForeignKey(People,on_delete=models.CASCADE)
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)

    def __str__(self):
        return self.people 


class Doctor(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.ForeignKey(People,on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name
    
class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_descri = models.CharField(max_length=500)

    def __str__(self):
        return self.p_name
    

class Bio(models.Model):
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    user = models. OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.user 
    