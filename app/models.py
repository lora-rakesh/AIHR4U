from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class EmployeeManager(BaseUserManager):
    def create_user(self, employee_id, password=None, **extra_fields):
        if not employee_id:
            raise ValueError('Employee ID is required')
        user = self.model(employee_id=employee_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Employee(AbstractBaseUser):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = []

    objects = EmployeeManager()

    def __str__(self):
        return self.employee_id
