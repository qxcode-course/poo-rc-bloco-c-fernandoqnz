class Kid:
    def __init__(self, nome: str, idd:int) -> None:
        self.nome= nome
        self.idd= idd

    def getIDDname(self) -> str:
        return f"{self.nome}:{self.idd}"
    
    def setIDDname(self, nome: str, idd:int):
        if nome.strip() and idd >=0:
            self.nome = nome
            self.idd = idd
        else:
            self.nome = "Ninguém"
            self.idd = 0


    def __str__(self) -> str:
        return f"Nome: {self.nome}, Idade: {self.idd}"
    

class Pula_pula:
    def __init__(self, c_esperando:int) -> None:
        self.esperando: list[Pula_pula | None]= []
        for _ in range(c_esperando):
            self.esperando.append(None)
            self.espera: list[Pula_pula]=[]
        self.brincando: list[Pula_pula | None]= []
        for _ in range(c_esperando):
            self.brincando.append(None)
            self.brinca: list[Pula_pula]=[]

    def entrar (self,pular: Pula_pula):
        self.espera.append(pular)

    def chamar(self, index:int):
        if index< 0 or index >= len(self.brincando):
            print("fail: pulapula inexistente")
            return
        if self.brincando[index] is not None:
            print("fail: pulapula ocupado")
        if len (self.espera )== 0:
            print(" fail: sem pulapulas")
        self.brincando[index] = self.espera[0]  
        del self.espera

    def finalizar(self, index:int):
        self.brincando[index]=None
        if index < 0 or index >= len(self.brincando):
            print("fail: pulapula inexistente")
            return
        if self.brincando[index] is None:
            print("fail: pulapula vazio")
            return
        
    def sair(self, nome: str) -> Pula_pula | None:
        for i, pular in enumerate(self.espera):
            if pular.nome == nome:
                del self.espera[i]
                return
            
    def __str__(self):
        return f"Pulapula(esperando: {self.esperando}, brincando: {self.brincando})"
        

def main():
    pula_pula = Pula_pula(3)
    while True:
        comando = input().strip().split()

        if comando[0] == "end":
            break
        elif comando[0] == "entrar":
            pula_pula.entrar(Pula_pula(comando[1], int(comando[2])))
        elif comando[0] == "chamar":
            pula_pula.chamar(int(comando[1]))
        elif comando[0] == "finalizar":
            pula_pula.finalizar(int(comando[1]))
        elif comando[0] == "sair":
            pula_pula.sair(comando[1])
        else:
            print("fail: comando invalido")
        print(pula_pula)

if __name__ == "__main__":
    main()
