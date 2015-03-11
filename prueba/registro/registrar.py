from registro.models import registro


def obtener_usuario(nuevo):
	try:
		us = registro.objects.get(nick=nuevo)
		return us
	except ValueError:
		return None
