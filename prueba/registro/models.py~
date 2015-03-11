from django.db import models

class registro(models.Model):
	usuario = models.CharField(max_length=50)
	nick = models.CharField(max_length=20)
	password = models.CharField(max_length=15)
	edad = models.IntegerField()
	def prueba_texto_sin_numeros(self):
		largo = len(self.usuario)
		numeros = 0
		nonumeros = 0
		for x in range(largo):
			if 47<ord(self.usuario[x])<57:
				numeros += 1
			else:
				nonumeros += 1
		return numeros
