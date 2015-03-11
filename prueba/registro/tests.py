from django.test import TestCase
from registro.models import registro
from registro import registrar

class pruebas_unitarias_registro(TestCase):

	def preparar(self):
		registro.objects.create(usuario='alejandro')
		registro.objects.create(usuario='juan perez')
	def test_usuario_no_numeros(self):
		self.preparar()
		regi = registro.objects.get(usuario='alejandro')
		regi2 = registro.objects.get(usuario='juan perez')
		self.assertEquals(regi.prueba_texto_sin_numeros(),0)
		self.assertEquals(regi2.prueba_texto_sin_numeros(),0)

	#def text_registro_no_existente(self):
	#	self.preparar()
	#	bueno = registrar.obtener_usuario('ale')
	#	malo = registrar.obtener_usuario('nadie')
	#	self.assertIsNone(malo)
	#	self.assertIsNotNone(bueno)
