from django.db import models


# Create your models here.

class Car_or_Bike(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    year=models.IntegerField()

    
    def __str__(self):
        return str(self.year)

class Vehicle(models.Model):
    type=models.ForeignKey(Car_or_Bike, on_delete=models.CASCADE,null=True, blank=True)
    Vehicle_name=models.CharField(max_length=50,null=True, blank=True)
    
    image=models.ImageField(upload_to='Vehice_images',null=True, blank=True)
    Rimage=models.ImageField(upload_to='Vehice_images',null=True, blank=True)
    Limage=models.ImageField(upload_to='Vehice_images',null=True, blank=True)
    Bimage=models.ImageField(upload_to='Vehice_images',null=True, blank=True)

    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    model=models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    year_of_manufacture=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=0)
    kilometers_driven=models.IntegerField()
    ownership_status=models.CharField(
        max_length=20, 
        choices=[('First Owner', 'First Owner'), ('Second Owner', 'Second Owner'), ('Third Owner & Above', 'Third Owner & Above')]
    )

    def __str__(self):
        return f"{self.brand.name} {str(self.model)} ({self.year_of_manufacture})"
