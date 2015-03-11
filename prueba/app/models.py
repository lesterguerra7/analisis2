from django.db import models

# Create your models here.
class Usuario(models.Model):
	usuario = models.CharField(max_length=256)
	password = models.CharField(max_length=30)
	algo = models.CharField(max_length=50)

