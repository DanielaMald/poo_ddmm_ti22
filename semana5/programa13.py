"""
    Programa13
    Nombre: Dulce Daniela MM
    Fecha: 08/02/2023
    Descripcion: clase Persona
"""
class Persona: #Crea la Clase Persona
    __email = None #Variable Privada_correo
    __nombre = None #Variable privada_nombre
    def __init__(self): #Constructor de la variable persona 
          print("Persona") #Imprime Persona
    def setEmail(self,email): #Constructor de la variable email
        self.__email = email # Variable privada email
    def setNombre(self,nombre): #Constructor de la variable nombre
        self.__nombre = nombre #Variable Privada nombre

    def getEmail(self): #Devuelve el valor email
       return self.__email #Returna a email
    def getNombre(self): #Devuelve el valor nombre
       return self.__nombre #Returna el nombre 


dejah = Persona() #Crea una Clase
dejah.setNombre("Dejah") #Guarda el nombre
print(dejah.getNombre()) #Imprime Deja 
dejah.setEmail("Dejah@utectulancingo.edu.mx") #Guarda el correo
print(dejah.getEmail()) #Imprime el email 
