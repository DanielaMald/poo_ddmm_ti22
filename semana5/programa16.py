"""
    Programa16
    Nombre: Dani Moctezuma
    Fecha: 14/02/2023
    Descripción: Crear un Clase persona y Alumno, imprimiendo su nombre, pelicula y correo
"""
class Persona: # Crea la Clase Persona 
    __nombre = None #Variable Privada 
    __edad = None # Variable Privada 
    def __init__(self): #Hace referencia a la clase / LLama a la clase 
       print("Persona") #Imprime persona

    def getNombre(self): #Se define una funcion para acceder a la variable privada y obtener un valor 
       return self._nombre #Return la variable 

    def setNombre(self,nombre): #Se define una funcion para acceder a la variable privada y llamarla
       self._nombre = nombre  #returna nombre 

    def getEdad(self):  #Se define una funcion para acceder a la variable privada y obtener un valor 
       return self._edad #Retorna edad 

    def setEdad(self,edad): #Se define una funcion para acceder a la variable privada y llamarla
       self._edad = edad #Retorna edad 

objeto_persona = Persona() 
#print(objeto_persona.nombre)
objeto_persona.nombre = "Hola"#Asigna una variable  una clase 
print(objeto_persona.nombre)#Asigna una variable  una clase 
objeto_persona.setNombre("Dani")#Asigna una variable  una clase 
print(objeto_persona.getNombre())#Asigna una variable  una clase 
objeto_persona.setEdad("19")#Asigna una variable  una clase 
print(objeto_persona.getEdad())#Asigna una variable  una clase 


class Alumno(Persona):
    __nombre = None
    __matricula = None
    def __init__(self):
       print("Alumno")

    def getNombre(self):
       return self._nombre

    def setNombre(self,nombre):
       self._nombre = nombre 

    def getMatricula(self):
       return self._matricula

    def setMatricula(self,matricula):
       self._matricula = matricula

objeto_alumno = Alumno()#Asigna una variable  una clase 
#print(objeto_alumno.nombre)
objeto_alumno.nombre = "Hola"#Asigna una variable  una clase 
print(objeto_alumno.nombre)#Asigna una variable  una clase 
objeto_alumno.setNombre("Dejah")#Asigna una variable  una clase 
print(objeto_alumno.getNombre())#Asigna una variable  una clase 
objeto_alumno.setMatricula("172212783")#Asigna una variable  una clase 
print(objeto_alumno.getMatricula())#Asigna una variable  una clase 


class Profesor(Persona):
    __nomina = None
    def __init__(self):
       print("Profesor")
    def getNomina(self):
       return self._nomina

    def setnomina(self,nomina):
       self._nomina = nomina

objeto_profesor = Profesor()
#print(objeto_profesor.nomina)
objeto_profesor.nomina = "5000$ al mes"
print(objeto_profesor.nomina)


class Coordinador:
    __numnomina = None
    __carrera_cordinador = None
    def __init__(self):
       print("Coordinador")
    def getNumNomina(self):
       return self._numnomina

    def setNumNomina(self,numnomina):
       self._numnomina = numnomina
      
    def getCarreraCor(self):
       return self._carrera_cordinador

    def setCarreraCor(self,carrera_cordinador):
       self._carrera_cordinador = carrera_cordinador
    
objeto_coordinador = Coordinador()
#print(objeto_coordinador.nomina)
objeto_coordinador.numnomina = "Ing. Salvador"#Asigna una variable  una clase 
print(objeto_coordinador.numnomina)#Asigna una variable  una clase 
objeto_coordinador.setNumNomina("5000 $")#Asigna una variable  una clase 
print(objeto_coordinador.getNumNomina())#Asigna una variable  una clase 
objeto_coordinador.setCarreraCor("Ing En Tecnolgias de la informacion")#Asigna una variable  una clase 
print(objeto_coordinador.getCarreraCor())#Asigna una variable  una clase 