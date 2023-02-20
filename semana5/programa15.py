"""
    Programa15
    Nombre: Daniela Moctezuma
    Fecha: 14/02/2023
    Descripción: Crear un Clase persona y Alumno, imprimiendo su nombre, pelicula y correo
"""
class Persona: #Crea la clase Persona
    __nombre = None #Variable Privada_nombre
    def __init__(self): #Constructor de la variable Persona 
         print("Persona")# Imprime Persona 

class Alumno(Persona): # Crea la clase alumno
    def __init__(self): #Constructor de la variable Alumno_Persona
          super().__init__() # Llama a la Clase  alumno 
          print("Alumno") #Imprime alumno 

objeto_persona = Persona() #Crea un objeto_persona
objeto_alumno = Alumno()#Crea un objeto_alumno

objeto_persona.nombre = "Dejah Thoris" #Da el valor del nombre Persona
print(objeto_persona.nombre) #Imprime el nombre 

objeto_alumno.nombre = "John Carter" #Da el valor de nombre Alumno
print(objeto_alumno.nombre)#Imrpime el nombre 

objeto_alumno.email = "John@gmail.com.mx"#Da el valor de email
print(objeto_alumno.email)#Da el valor del correo

print(dir(objeto_persona))#Muestra lo que hay dentro de la clase persona 
print(dir(objeto_alumno))#Muestra lo que hay dentro de la clase alumno.