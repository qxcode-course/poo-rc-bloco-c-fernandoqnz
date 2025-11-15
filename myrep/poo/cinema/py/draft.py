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
            print("fail: assento inexistente")
            return False

        return True
    
    def search(self, id:str) ->int:
        for i, client in enumerate(self.seats):
            if client is not None and client.getID()== id:
                return i
        return -1
    
    def reserve(self, id:str, nmr:int, index:int):
        if not self.verifyIndex(index):
            return
        
        if self.search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return
        
        client = Client(id, nmr)
        self.seats[index]=client

    def cancel(self, id:str):
        index = self.search(id)
        if index == -1:
            print("fail: cliente nao esta no cinema")
            return
        self.seats[index]=None

    def getSeats(self):

