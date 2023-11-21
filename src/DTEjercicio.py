class DTEjercicio:
    def __init__(self, Id, descripcion, ejercicio = None):
       self.__Id = Id
       self.__Descripcion = descripcion
       
    def getDescripcion(self):
        return self.__Descripcion
    
    