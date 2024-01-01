from django.db import models

# Create your models here.
 
class Marque(models.Model):
    id_marque = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    logo = models.FileField(upload_to='photos/%y/%m/%d', default=0)
    def __str__(self):
        return self.nom

class Model(models.Model):
    id_model = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    annee = models.IntegerField()
    ENERGIE_CHOICES = [
        ('Essence', 'essence'),
        ('Diesel', 'diesel'),]
    VITESSE_CHOICES = [
        ('Manual', 'manual'),
        ('Automatic', 'automatic'),]
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.FileField(upload_to='photos/%y/%m/%d')
    image1 = models.FileField(upload_to='photos/%y/%m/%d',null=True, blank=True)
    image2 = models.FileField(upload_to='photos/%y/%m/%d',null=True, blank=True)
    image3 = models.FileField(upload_to='photos/%y/%m/%d',null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    puissance = models.IntegerField()
    energie = models.CharField(choices=ENERGIE_CHOICES, max_length=20)
    nbr_plc = models.IntegerField()
    vitesse = models.CharField(choices=VITESSE_CHOICES, max_length=20)
    speed = models.DecimalField(max_digits=2,decimal_places=1)
    id_marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
min_place = 2
max_place = 7
nbr_place = Model.objects.filter(nbr_plc__range=(min_place, max_place))
