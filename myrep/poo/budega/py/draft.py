class Person:
    def __init__(self, nome: str) -> None:
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome.strip() if nome.strip() else "Ninguém"

    def __str__(self) -> str:
        return f"{self.__nome}"


class Budega:
    def __init__(self, num_caixas: int) -> None:
        self.caixas: list[Person | None] = [None for _ in range(num_caixas)]
        self.espera: list[Person] = []

    def entrar(self, person: Person):
        self.espera.append(person)

    def chamar(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        self.caixas[index] = self.espera.pop(0)

    def finalizar(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return
        self.caixas[index] = None

    def sair(self, nome: str):
        for i, person in enumerate(self.espera):
            if person.getNome() == nome:
                del self.espera[i]
                return
        print("fail: cliente não encontrado")

    def __str__(self):
        caixas_str = ", ".join([str(p) if p else "-" for p in self.caixas])
        espera_str = ", ".join([str(p) for p in self.espera])
        return f"[{caixas_str}] => Espera: [{espera_str}]"

def main():
    budega = Budega
    while True:
        line=input()
        args =line.split(" ")
        print(f"${' '.join(args)}")
        cmd= args[0]

        if cmd == "show":
            print(budega)
        elif cmd=="call":
            budega.chamar
        elif cmd== "finish":
            budega.finalizar
        elif cmd== "init":
            budega.__init__
        elif cmd=="end":
            break
        



            