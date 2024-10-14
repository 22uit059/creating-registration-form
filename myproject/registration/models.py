from django.db import models

# Create your models here.



class UserRegistration(models.Model):
  username = models.CharField(max_length=100)
  email = models.EmailField()
  password = models.CharField(max_length=100)
  def _str_(self):
        return self.name