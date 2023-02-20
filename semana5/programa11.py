"""
    Programa11
    Nombre: Dulce Daniela MM
    Fecha: 08/02/2023
    Descripcion: clase Persona
"""
class Persona:
	__nombre = None
	__email = None
	def __init__(self):
		print("Persona")
	def setNombre(self, nombre):
	    self.__nombre = nombre

	def getNombre(self):
	    return self.__nombre
	
	def setEmail(self,email):
	    self.__email = email

	def getEmail(self):
	    return self.__email



dejah = Persona()
dejah.setNombre("Dejah")
dejah.setEmail("daniela02maldonado.moctezuma@gmail.com")
print(dejah.getNombre())
print(dejah.getEmail())