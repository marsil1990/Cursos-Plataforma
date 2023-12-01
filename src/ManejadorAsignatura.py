from src.Asignatura import Asignatura
class ManejadorAsignatura(object):
    __instancia = None
    __MAPAsignaturas = None
    
    def __new__(cls):
        if ManejadorAsignatura.__instancia is None:
            ManejadorAsignatura.__instancia = object.__new__(cls)
            ManejadorAsignatura.__MAPAsignaturas = dict()
        return ManejadorAsignatura.__instancia
    


    def getInstancia(): pass
    def agregarAsignatura(self, asignatura):
        self.__MAPAsignaturas[asignatura.getNombre()] = asignatura

    def SETAsignaturasDisponibles(self):
        SETAsignaturas  = set()
        for i in self.__MAPAsignaturas.values():
            nomIdioma = i.getNombre()#.strip().lower()
            SETAsignaturas.add(nomIdioma)
        return SETAsignaturas

        
    def obtenerAsignatura(self, nombreAsignatura):
        return self.__MAPAsignaturas[nombreAsignatura]
        

    def existeAsignatura(self, nombreAsignatura):
        nombre_minuscula = nombreAsignatura#.lower().strip()
        setAsignatura = self.SETAsignaturasDisponibles()
        return nombre_minuscula in setAsignatura
            
    #def __del__(): pass

