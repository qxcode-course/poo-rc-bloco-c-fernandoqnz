class Person:
    def __init__(self, name:str) -> None:
        self.__name=name 
    
    def getNome(self)->str:
        return self.__name
    
    def setName(self,name:str):
        return self.__name

    
    def __str__(self) -> str:
        return f"{self.__name}"
        
