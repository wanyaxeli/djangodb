from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import check_password 
# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255)
    
    objects = UserManager()
    check_password(password)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ["first_name", "last_name",]
    def __str__(self):
        return self.first_name

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True
    
    