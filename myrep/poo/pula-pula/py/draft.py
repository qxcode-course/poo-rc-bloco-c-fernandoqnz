class Kid:
    def __init__(self, nome: str, idd: int) -> None:
        self.nome = nome
        self.idd = idd

    def __str__(self) -> str:
        return f"{self.nome}:{self.idd}"


class Pula_pula:
    def __init__(self, capacidade: int) -> None:
        self.capacidade = capacidade
        self.brincando: list[Kid | None] = [None for _ in range(capacidade)]
        self.espera: list[Kid] = []

    def entrar(self, kid: Kid):
        self.espera.append(kid)

    def chamar(self, index: int):
        if index < 0 or index >= len(self.brincando):
            print("fail: índice inexistente")
            return
        if self.brincando[index] is not None:
            print("fail: ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem crianças esperando")
            return
        self.brincando[index] = self.espera.pop(0)

    def finalizar(self, index: int):
        if index < 0 or index >= len(self.brincando):
            print("fail: índice inexistente")
            return
        if self.brincando[index] is None:
            print("fail: vazio")
            return
        self.brincando[index] = None

    def sair(self, nome: str):
        for i, kid in enumerate(self.espera):
            if kid.nome == nome:
                del self.espera[i]
                return
        print("fail: criança não encontrada")

    def __str__(self):
        brincando = ", ".join([str(kid) if kid else "-" for kid in self.brincando])
        esperando = ", ".join([str(kid) for kid in self.espera])
        return f"[ {brincando} ] => Espera: [ {esperando} ]"


    
        
