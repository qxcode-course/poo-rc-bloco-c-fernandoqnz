class Person:
    def __init__(self,nome:str) -> None:
        try:
            if nome=="":
                raise Exception("fail: nome não pode ser vazio")
        except Exception as e:
            print(e)
        self.__nome=nome

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome:str):
        try:
            if nome.strip()=="":
                raise Exception("fail: nome não pode ser vazio")
        except Exception as e:
            print(e)
        self.__nome = nome


    def __str__(self) -> str:
        return f"{self.__nome}"

class Market: 
    def __init__(self, nbox:int) -> None:
        self.box: list[Person | None] = []
        for  _ in range(nbox):
            self.box.append(None)
        self.waiting: list[Person] = []
    
    def arrive(self, person: Person):
        self.waiting.append(person)


    def call(self, index:int):
        
        if len(self.waiting) == 0:
            print("fail: sem clientes")
            return

        if index < 0 or index >= len(self.box):
            print("fail: caixa inexistente")
            return

        if self.box[index] is not None:
            print("fail: caixa ocupado")
            return

        self.box[index] = self.waiting.pop(0)




    def finish(self, index:int):
        if index < 0 or index >= len(self.box):
            print("fail: caixa inexistente")
            return

        if self.box[index] is None:
            print("fail: caixa vazio")
            return

        self.box[index] = None

    def give_up(self, nome:str):       
        for i, pessoa in enumerate (self.waiting):
            if pessoa.getNome() == nome:
                self.waiting.pop(i)
                return

    
    def __str__(self):
        box =", ".join(["-----" if x is None else str(x) for x in self.box])
        wait= ", ".join([str(x) for x in self.waiting])

        return f"Caixas: [{box}]\nEspera: [{wait}]"

def main():
    market=Market(0)
    while True:
        line=input()
        args=line.split(" ")
        print(f"${' '.join(args)}")
        cmd= args[0]

        if cmd == "end":
            break
        if cmd == "show":
            print(market)
        if cmd == "init":
            market=Market(int(args[1]))
        if cmd == "arrive":
            nameclient= args[1]
            market.arrive(Person(nameclient))
        if cmd == "call":
             market.call(int(args[1]))
        if cmd=="finish":
            market.finish(int(args[1]))
        if cmd=="giveup":
            market.give_up(args[1])

main()

    