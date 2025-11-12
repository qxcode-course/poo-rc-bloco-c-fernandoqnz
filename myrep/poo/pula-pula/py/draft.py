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

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__idade}"
    
class Pula_pula:
    def __init__(self) -> None:
        self.espera: list[Kid] = []
        self.pular: list[Kid] = []

    def criar(self, kid: Kid):
        self.espera.append(kid)
    
    def chamar(self):
        try:
            if len(self.espera) <= 0:
                raise Exception ("fail: fila vazia")
            self.pular.append(self.espera.pop(0))
        except Exception as e:
            print(e)
            
    def sair(self):
        try:
            if len(self.pular) <= 0:
                raise Exception ("fail: ninguem brincando")
            self.espera.append(self.pular.pop(0))
        except Exception as e:
            print(e)

    def remove(self, nome:str):
        for i, kid in enumerate (self.pular):
            if kid.getNome() == nome:
                self.pular.pop(i)
                return 
        
        for i, kid in enumerate (self.espera):
            if kid.getNome() == nome:
                self.espera.pop(i)
                return
            
        print(f"fail:{nome} nao esta no pula-pula")
                  
                
    def __str__(self) -> str:
        espera = " ,".join(str(kid) for kid in self.espera) 
        pular = " ,".join(str(kid) for kid in self.pular)

        return f"[{espera}]=> [{pular}]"
    



def main():
    pula_pula=Pula_pula() 
    while True:
        line=input()
        args=line.split(" ")
        print (f"${args[0]}")
        cmd= args[0]
        if cmd =="show":
            print(pula_pula)  
        elif cmd=="arrive":
            nome = args[1]
            idade = int(args[2])
    
            pula_pula.criar(Kid(nome, idade))
        
        elif cmd=="leave":
            pula_pula.sair()
        elif cmd=="remove":
            pula_pula.remove(args[1])
        elif cmd=="enter":
            pula_pula.chamar()

            
            

if __name__ == "__main__":
    main()


        
            
            


            


        


