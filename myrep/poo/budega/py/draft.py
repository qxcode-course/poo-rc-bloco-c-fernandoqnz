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

    def call(self):
        try:
            if len(self.waiting) <=0:
                raise Exception("fail : fila vazia")
            elif None not in self.box:
                raise Exception("fail: caixa ocupado")


            else:
                for i in range(len(self.box)):
                    if self.box[i] is None:
                        self.box[i] = self.waiting.pop(0)
                        
                        return
            for i in range(len(self.box)):
                if self.box[i] is not None:
                    print("fail: caixa ocupado")
                    return

            
        except Exception as e:
            print(e)

    def finish(self, index:int):
        self.box[index]= None
        try:
            if index < 0 or index>= len(self.box):
                raise Exception("fail: caixa inexistente")
            elif self.box[index] is None:
                return
        except Exception as e:
            print(e)

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
        if cmd== "call":
            market.call()
        if cmd=="finish":
            market.finish(int(args[1]))
        if cmd=="giveup":
            market.give_up(args[1])

main()

    