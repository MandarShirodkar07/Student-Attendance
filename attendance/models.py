from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.name

class Degree(models.Model):
    name = models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.name

class Faculty(AbstractUser):  # Extending Django's built-in User model
    email= models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="faculty_groups",  # Add a unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="faculty_permissions",  # Add a unique related name
        blank=True
    )

    def __str__(self):
        return self.username