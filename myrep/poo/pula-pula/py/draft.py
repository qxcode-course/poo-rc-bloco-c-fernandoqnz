class Kid:
    def __init__(self, nome:str, idade:int):
        self.__nome = nome
        self.__idade = idade
    
    def getIdd(self)->str:
        return self.__nome

    def getNome (self)->int:
        return self.__idade

    def setNome(self, nome:str):
        self.__nome = nome
    
    def __str__(self) -> str:
        return f"{self.__nome} e {self.__idade}"

class Pula_pula:
    def __init__(self, num_brincando:int) -> None:
        self.brincando: list[Kid | None] = [None for _ in range(num_brincando)]
        self.espera: list[Kid] = []

    def entrar(self, kid: Kid):
        self.espera.append(kid)

    def chamar(self, index:int):
        if index < 0 or index >= len(self.brincando):
            print("fail: ninguém brincando")
            return
        
        if self.brincando[index] is not None:
            print("")

    