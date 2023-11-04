from src.asignatura import Asignatura
class ManejadorAsignatura(object):
    __instancia = None
    __MAPAsignaturas = {}
    
    def __new__(cls):
        if ManejadorAsignatura.__instancia is None:
            ManejadorAsignatura.__instancia = object.__new__(cls)
        return ManejadorAsignatura.__instancia
    


    def getInstancia(): pass
    def agregarAsignatura(self, Asignatura):
        self.__MAPAsignaturas[Asignatura.getNombre()] = Asignatura

    def SETAsignaturasDisponibles(self):
        SETAsignaturas  = set()
        for i in self.__MAPAsignaturas.values():
            SETAsignaturas.add(i.getNombre().strip().lower())
        return SETAsignaturas

        
    def obtenerAsignatura(self, nombreAsignatura):
        return self.__MAPAsignaturas[nombreAsignatura]

    def existeAsignatura(self, nombreAsignatura):
        nombre_minuscula = nombreAsignatura.lower().strip()
        setAsignatura = self.SETAsignaturasDisponibles()
        return nombre_minuscula in setAsignatura
            
    #def __del__(): pass

