

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        DEVELOPER = "developer", "Developer"
        TESTER = "tester", "Tester"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.TESTER)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
