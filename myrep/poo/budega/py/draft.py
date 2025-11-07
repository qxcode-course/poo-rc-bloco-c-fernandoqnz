class Person:
    def __init__(self, nome:str) -> None:
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setNome(self, nome:str):
        if nome.strip():
            self.__nome = nome
        else:
            self.__nome = "Ninguém"

    def __str__(self) -> str:
        return f"Nome: {self.__nome}"

class Budega:
    def __init__(self,num_caixas:int) -> None:
        self.caixas: list[Person | None]= []
        for _ in range(num_caixas):
            self.caixas.append(None)
            self.espera: list[Person]=[]
    
    def entrar (self, person :Person):
        self.espera.append(person)

    def chamar(self, index:int):
        if index< 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
        if len (self.espera )== 0:
            print(" fail: sem clientes")
        self.caixas[index] = self.espera[0]  
        del self.espera

    def finalizar(self, index:int):
        self.caixas[index]=None
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return
        
    def sair(self, nome: str) -> Person | None:
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                del self.espera[i]
                return
            
    def __str__(self):
        caixas = ", ".join([str(x) if x else "----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.])


    def main():        budega = Budega(3)
        while True:
            comando = input().strip().split()
            if comando[0] == "end":
                break
            elif comando[0] == "entrar":
                mercantil.entrar(Person(comando[1]))
            elif comando[0] == "chamar":
                budega.chamar(int(comando[1]))
            elif comando[0] == "finalizar":
                budega.finalizar(int(comando[1]))
            elif comando[0] == "sair":
                budega.sair(comando[1])
                
            else:
                print("fail: comando invalido")
            print(budega)
            
