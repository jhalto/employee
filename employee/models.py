from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length= 300)

    class Meta():
        ordering = ['name']
        # verbose_name_plural = "Departe"
    def __str__(self):
        return f"{self.name}-{self.location}"

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to= 'employee_images', default= 'images.jpg')
    address = models.CharField(max_length=300)
    department = models.ForeignKey(Department, on_delete= models.SET_NULL, null= True, blank= True)
    manager = models.ForeignKey('self', on_delete= models.SET_NULL , null= True , blank= True)
     
    class Meta():
        ordering = ['id']
        # verbose_name_plural = "Daldfkja"

    def full_name(self):
        return f"{self.first_name}-{self.last_name}"
    
    def __str__(self):
        return self.first_name

