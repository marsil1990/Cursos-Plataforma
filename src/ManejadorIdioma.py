from src.Idioma import Idioma
class ManejadorIdioma(object):
    __instancia = None
    __MAPIdiomas = {}
    
    def __new__(cls):
        if ManejadorIdioma.__instancia is None:
            ManejadorIdioma.__instancia = object.__new__(cls)
        return ManejadorIdioma.__instancia
    


    def getInstancia(): pass
    def agregarIdioma(self, idioma):
        self.__MAPIdiomas[idioma.getNombre()] = idioma

    def SETIdiomasDisponibles(self):
        SETidiomas  = set()
        for i in self.__MAPIdiomas.values():
            SETidiomas.add(i.getNombre().strip().lower())
        return SETidiomas

        
    def obtenerIdioma(nombreIdioma): pass

    def existeIdioma(self, nombreIdioma):
        nombre_minuscula = nombreIdioma.lower().strip()
        setIdiom = self.SETIdiomasDisponibles()
        return nombre_minuscula in setIdiom
            
    #def __del__(): pass

