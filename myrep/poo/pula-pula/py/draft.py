class Kid:
    def __init__(self,nome:str, idade:int) -> None:
        if nome== "":
            raise Exception("fail: nome não pode ser vazio")
            
        elif idade <= 0:
            raise Exception("fail: idade inválida")
            

        self.__nome =nome 
        self.__idade=idade

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade 
    
    def setNome(self, nome:str):
        if nome.strip() == "":
            raise Exception ( " fail: nome vazio")
        self.__nome = nome
    def setIdade(self, idade:int):
        if idade <= 0:
            raise Exception(" fail: idade inválida")
        self.__idade =idade
    
class Pula_pula:
    def __init__(self) -> None:
        self.espera: list[Kid] = []
        self.pular: list[Kid] = []

    def entrar(self, kid: Kid):
        self.espera.append(kid)
    
    def chamar(self):
        try:
            if len(self.espera) <= 0:
                raise Exception ("fail: fila vazia")
            self.pular.append(self.espera.pop(0))
        except Exception as e:
            print(e)
            
    def sair(self ):
        try:
            if len(self.pular) <= 0:
                raise Exception ("fail: ninguem brincanado")
            self.espera.append(self.pular.pop(0))
        except Exception as e:
            print(e)
                
            #testando a sintaxe de cima
            #self.espera.append(self.pular.pop(0))
            #try:
            #    if len(self.pular) <=0:
            #    raise Exception ("fail: ninguem brincando")
            #except Exception as e:
            #    print(e
            
            


            


        


