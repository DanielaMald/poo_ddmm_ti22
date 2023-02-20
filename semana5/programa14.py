"""
    Programa14
    Nombre: Daniela Moctezuma
    Fecha: 13/02/2023
    Descripción: Crear un Clase Alumno, imprimiendo su nombre, matricula y carrera
"""
class Alumno: #Clase alumno 
    __nombre = None #Variable Privada_nombre
    __matricula = None #Variable Privada_matricula
    __carrera= None #Variable Privada_carrera
    def __init__(self): #Constructor de la variable alumno
          print("Alumno")#Imprime Alumno
    def setNombre(self,nombre): #constructor de la variable nombre
        self.__nombre = nombre #Variable Privada nombre
    def setMatricula(self,matricula): #Constructor de la variable matricula 
        self.__matricula = matricula #Variable Privada matricula
    def setCarrera(self,carrera): # Constructor de la variable carrera
        self.__carrera = carrera # Variable Privada Carrera

    def getNombre(self): #Constructor de la variable alumno
        return self.__nombre #Variable Privada Nombre
    def getMatricula(self): #Constructor de la variable alumno
        return self.__matricula #Variable Privada Matricula
    def getCarrera(self): #Constructor de la variable alumno
        return self.__carrera #Variable Privada Carrera

dejah = Alumno() #Crea un objeto
dejah.setNombre("Dejah") #Guarda la variable 
print(dejah.getNombre()) #Imprime Dejah
dejah.setMatricula("12109293") #Guarda la variable para imprimir
print(dejah.getMatricula()) #Imprime Matricula
dejah.setCarrera("Ing. Informatica") #Guarda la variable para imprimir
print(dejah.getCarrera()) # Imprime Carrera