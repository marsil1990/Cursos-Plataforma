class DTEjercicio:
    def __init__(self, Id = None, descripcion=None, ejercicio = None):
        if ejercicio is None:
            self.__Id = Id
            self.__Descripcion = descripcion
        else:
            self.__Id = ejercicio.getId()
            self.__Descripcion = ejercicio.getDescripcion()
       
    def getDescripcion(self):
        return self.__Descripcion
    def getId(self):
        return self.__Id
    
    