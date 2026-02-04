from django.db import models
from django.core.validators import EmailValidator

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    department = models.CharField(max_length=30)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.employee_id} - {self.full_name}"
    
    
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', "Present"),
        ('Absent', "Absent"),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
        unique_together = ('employee', 'date')  # Prevent duplicate attendance per day
    
    def __str__(self):
        return f"{self.employee.full_name} - {self.date} {self.status}"