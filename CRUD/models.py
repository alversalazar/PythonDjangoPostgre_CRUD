from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Carrer(models.Model):
    name = models.CharField(max_length=50, null=False)
    duration = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, null=False)
    status = models.BooleanField(null=True)
    idUser = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table ='carrer'
        ordering = ['id']
        
class Employee(models.Model):
    name = models.CharField(max_length=50, null=False)
    firstname = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=False)
    socialsegurity = models.CharField(max_length=11, null=False)
    dateofhire = models.DateTimeField(null=False)
    status = models.BooleanField(null=True)
    idUser = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table ='employee'
        ordering = ['id']
        

class Subject(models.Model):
    name = models.CharField(max_length=50, null=False)
    credit = models.CharField(max_length=50, null=False)
    unit = models.CharField(max_length=50, null=False)
    characteristic = models.CharField(max_length=50, null=False)
    keymatter = models.CharField(max_length=50, null=False)
    status = models.BooleanField(null=True)
    idUser = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table ='subject'
        ordering = ['id']
        
        
class Studyplan(models.Model):
    objetive = models.CharField(max_length=100, null=False)
    datestart = models.DateTimeField(null=False)
    datefinal = models.DateTimeField(null=False)
    key = models.CharField(max_length=20, null=False)
    idCarrer = models.ForeignKey(Carrer,on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(null=True)
    idUser = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.objetive
    
    class Meta:
        db_table ='studyplan'
        ordering = ['id']
        

class Viatic(models.Model):
    place = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=150, null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    idEmployee = models.ForeignKey(Employee,on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(null=True)
    idUser = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    modifieddate = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.place
    
    class Meta:
        db_table ='viatic'
        ordering = ['id']