from django.db import models
from datetime import date
from products.models import Model
# Create your models here.


class User(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
    

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    cin = models.CharField(max_length=50)
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    SEXE_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),]
    sexe  = models.CharField(choices=SEXE_CHOICES,max_length=10)
    telephone = models.IntegerField()
    email = models.EmailField(max_length=100)
    Reservation_Date = models.DateField(default=date.today)
    ModelName = models.ForeignKey(Model, on_delete=models.CASCADE)
    def __str__(self):
        return self.cin
