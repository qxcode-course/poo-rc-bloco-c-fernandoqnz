class Lead:
    def __init__(self, thickness:float, hardness:str, size:int) -> None:
        self.__thickness= thickness
        self.__hardness = hardness
        self.__size=size

    def getThickness(self) ->float:
        return self.__thickness
    
    def getHardness(self) -> str:
        return self.__hardness

    def getSize(self) -> int:
        return self.__size
    
    def setSize(self, size: int):
        self.__size =size

    def usageSheet(self ) -> int:
        if self.__hardness == "HB":
            return 1
        if self.__hardness =="2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6
        return 0
    
    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

class Pencil:
    def __init__(self, thickness:float) -> None:
        self.__thickness = thickness
        self.__bico= None
        self.__drum = []

    def insert(self, gft):
        if gft.getThickness() != self.__thickness:
            print("fail: calibre incompatível")
            return False
        self.__drum.append(gft)
        return True

    def remove(self):
        if self.__bico is not None:
            gft_removed = self.__bico
            self.__bico = None
            return gft_removed
        return None
    
    def pull(self):
        if self.__bico is not None:
            print("fail: ja existe grafite no bico")
            return False
        
        if not self.__drum:
            print("fail: tambor esta vazio")
            return False
        
        pull_gft = self.__drum[0]
        self.__bico  = pull_gft
        self.__drum = self.__drum[1:]
        return True
    
    def writePage(self):
        if self.__bico is None:
            print("fail: nao existe grafite no bico")
            return 
        
        current_size = self.__bico.getSize()
        if current_size <= 10:
            print("fail: tamanho insuficiente")
            self.remove()
            return
        
        wear = self.__bico.usageSheet()
        new_size = current_size - wear

        if new_size < 10:
            print("fail: folha incompleta")
            self.__bico.setSize(10)
            self.remove
        else:
            self.__bico.setSize(new_size)

    def show(self):
        tip_str = str(self.__bico) if self.__bico else "[]"
        barrel_str  = "".join(str(lead) for lead in self.__drum)
        print(f"calibre: {self.__thickness}, bico: {tip_str}, tambor: <{barrel_str}>")

def main():
    pencil=Pencil(0)
    while True:
        line=input()
        print(f"${line}")
        args=line.split()

        if len(args)== 0:
            continue

        cmd = args[0]

        if cmd == "end": 
         break
        elif cmd =="init":
            pencil=Pencil(float(args[1]))
        elif cmd == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            lead = Lead(thickness, hardness, size)
            pencil.insert(lead)

        elif cmd =="pull":
            if pencil:
                pencil.pull()

        elif cmd == "remove":
            pencil.remove()

        elif cmd == "write":
            pencil.writePage()

        elif cmd == "show":
            pencil.show()

if __name__ == "__main__":
    main()

    

            



        

    
