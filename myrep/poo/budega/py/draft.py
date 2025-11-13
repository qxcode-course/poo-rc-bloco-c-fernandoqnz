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

    def __str__(self) -> str:
        return f"{self.__nome}"

class Market: 
    def __init__(self, nbox:int) -> None:
        self.box: list[Person | None] = []
        for  _ in range(nbox):
            self.box.append(None)
        self.waiting: list[Person]
    
    def arrive(self, person: Person):
        self.waiting.append(person)

    def call(self):
        try:
            if len(self.waiting) <=0:
                raise Exception("fail : fila vazia")
            elif len(self.waiting) is not 0:
                raise  Exception("fail: sem clientes")
            elif len(self.waiting) == len(self.box):
                raise Exception("fail: caixa ocupado")
            
            self.box.append(self.waiting.pop(0))
        except Exception as e:
            print(e)

    def finish(self, index:int):
        self.box[index]= None
        try:
            if index < 0 or index>= len(self.box):
                raise Exception("fail: caixa inexistente")
            elif self.box[index] is None:
                raise Exception("fail: caixa vazio")
        except Exception as e:
            print(e)

    def give_up(self, nome:str):       
        for i, pessoa in enumerate (self.waiting):
            if pessoa.getNome() == nome:
                self.waiting.pop(i)
                return

    
    def __str__(self):
        boxes_str = "[" + ", ".join(
            c.getNome() if c is not None else "-----" for c in self.box
        ) + "]"
        queue_str = "[" + ", ".join(p.getNome() for p in self.waiting) + "]"
        return f"Caixas: {boxes_str}\nEspera: {queue_str}"

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

    