from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)