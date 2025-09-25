class cliente:
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def __setNombre(self,nombre):
        self.__nombre = nombre
    
    def __getNombre(self):
        return self.__nombre  
    
    def __setApellido(self,apellido):
        self.__apellido = apellido
    
    def __getApellido(self):
        return self.__apellido

