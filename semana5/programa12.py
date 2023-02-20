"""
    Programa12
    Nombre: Dulce Daniela MM
    Fecha: 08/02/2023
    Descripcion: herencia Persona
"""

from persona import Persona

class Profesor(Persona): #crea la clase Profesor que hereda de la clase Persona
    def __init__(self) -> None: #constructor de  la clase Profesor
        super().__init__() #llama al constructor de persona
        print("Profesor") #imprime el texto Profesor

objeto_profesor = Profesor() #crea un objeto de la clase Profesor 
