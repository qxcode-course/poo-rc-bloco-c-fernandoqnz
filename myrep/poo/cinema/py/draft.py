class Client:
    def __init__(self, id:str, nmr:str) -> None:
        if id == "":
            raise Exception ("fail : id invalido")
        
        elif nmr == "":
            raise Exception("fail : numero invalido ")
        
        self.__id = id
        self.__nmr = nmr
        
    def getID(self):
        return self.__id
    
        
    def getNmr(self):
        return self.__nmr

    def setID(self, id:str):
        if id.strip()=="":
            raise Exception ("fail : id invalido")
        self.__id = id

    def setNmr(self, nmr:str):
        if nmr.strip()=="":
            raise Exception ("fail : numero invalido")
        self.__nmr = nmr
    
class Sala:
    def __init__(self, max_capacity:int) -> None:
        self.seats: list[Client | None] = [None for _ in range(max_capacity)]

    def reserve(self, client:Client):
        self.seats.append(client)

    def cancel(self):
        try:
            if len(self.seats) <= 0:
                raise Exception ("fail: ninguem na sala")
            self.seats.pop()
        except Exception as e:
            print(e)




