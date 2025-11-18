class Client:
    def __init__(self, id: str, nmr: int) -> None:
        if id == "":
            raise Exception("fail: id invalido")

        if nmr <= 0:
            raise Exception("fail: numero invalido")

        self.__id = id
        self.__nmr = nmr
        
    def getID(self):
        return self.__id
    
    def getNmr(self):
        return self.__nmr

    def setID(self, id: str):
        if id.strip() == "":
            raise Exception("fail: id invalido")
        self.__id = id

    def setNmr(self, nmr: int):
        if nmr <= 0:
            raise Exception("fail: numero invalido")
        self.__nmr = nmr

    def __str__(self) -> str:
        return f"{self.__id}:{self.__nmr}"

    
class Theather:
    def __init__(self, maxcapacity:int) -> None:
        self.seats: list[Client | None] = []
        for  _ in range(maxcapacity):
            self.seats.append(None)

    def verifyIndex(self, index: int):
        if len(self.seats) == 0:
            print("fail: sem assentos")
            return False
        
        if index < 0 or index >= len(self.seats):
           # print("fail: assento inexistente")
            return False

        return True
    
    def search(self, id:str) ->int:
        for i, client in enumerate(self.seats):
            if client is not None and client.getID()== id:
                return i
        return -1
    
    def reserve(self, id:str, nmr:int, index:int):
        
        
        if not self.verifyIndex(index):
            print("fail: cadeira nao existe")
            return False
        
        if self.seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        
        if self.search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return False

            
        client = Client(id, nmr)
        self.seats[index]=client


    def cancel(self, id:str):
        index = self.search(id)
        if index == -1:
            print("fail: cliente nao esta no cinema")
            return
        self.seats[index]= None

    def getSeats(self):
        return self.seats
    
    def __str__(self) -> str:
        content = " ".join(str(client) if client is not None else "-"
                           for client in self.seats)
        return f"[{content}]"
    
def main():
    tt= Theather(0)
    while True:
        line=input()
        args= line.split(" ")
        print(f"${' '.join(args)}")
        cmd = args[0]

        if cmd =="show":
            print(tt)
        
        elif cmd =="end":
            break

        elif cmd =="init":
            tt=Theather(int(args[1]))
            
        elif cmd=="reserve":
            id=args[1]
            nmr= int(args[2])
            index= int(args[3])
            tt.reserve(id, nmr,index)

        elif cmd =="cancel":
            tt.cancel(args[1])

main()



        
