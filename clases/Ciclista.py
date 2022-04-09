class Ciclista:

    def __init__(self):
        self.__nombre=None
        self.__edad=None
        self.__pais=None
        self.__tiempo=None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def pais(self):
        return self.__pais

    @property
    def tiempo(self):
        return self.__tiempo

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @edad.setter
    def edad(self,edad):
        if(edad < 0):
            print("Digite edad valida no permito numeros negativos")
        else:
            self.__edad=edad

    @pais.setter
    def pais(self,pais):
        self.__pais=pais

    @tiempo.setter
    def tiempo(self,tiempo):
        self.__tiempo=tiempo