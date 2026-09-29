from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=20)
    
    
class Capital(models.Model):
    country = models.OneToOneField(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
  
  
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    # def __str__(self):
    #     return self.name
    
 
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    mfg = models.DateField(null=True)
    brand = models.CharField(default="all")
    
    # def __str__(self):
    #     return f"{self.name} {self.price}"
    
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    
    
class Course(models.Model):
    student = models.ManyToManyField(Student)
    name = models.CharField(max_length=20)
    
    
    