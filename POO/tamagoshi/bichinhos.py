from tamagoshi import Tamagoshi

class Dragao(Tamagoshi):
    def __init__(self, nome, saude, fome, idade, tedio):
        super().__init__(nome, saude, fome, idade, tedio)
        self.banho = 50
        self.sede = 0
        self.saude = 200
        self.temperamento = 0

    def mostrarInfo():
        print("")
        print(f"------------ {({self.nome}).upper()} ------------")
        print(f"[Idade]: [{self.idade}]\n[Fome]: [{self.fome}]\n[Sede]: [{self.sede}]\n[Banho]: [{self.banho}]\n[Saúde]: [{self.saude}]\n[Tédio]: [{self.tedio}]\n[Temperamento]: [{self.temperamento}]")
        print("-------------------------------")
        print("")
        
    def banho(self, qtd):
        if (self.banho == 0):
            print(f"{self.nome} não quer tomar banho agora.")
        elif (qtd + self.banho <= 100):
            self.banho += self.banho * (qtd/50)
            print(f"{self.nome} tomou um banhinho rápido.")
        else:
            self.banho = 100
            print(f"{self.nome} tomou banho e está cheirosinho!")

    def beberAgua(self, qtd):
        if (self.sede == 0):
            print(f"{self.nome} não está com sede.")
        else:
            self.sede -= qtd
            print(f"{self.nome} bebeu {qtd} litros de água.")

    def voar(self):
        self.tedio -= 10
        self.fome += 5
        self.sede += 5

    def soltar_fogo(self):
        self.tedio -= 20
        self.temperamento -= 20

# ----------------------------------------------------

class Pou(Tamagoshi):
    def __init__(self, nome, saude, fome, idade, tedio):
        super().__init__(nome, saude, fome, idade, tedio)
        self.banho = 50
        self.sede = 0
        
    def mostrarInfo():
        print("")
        print(f"------------ {({self.nome}).upper()} ------------")
        print(f"[Idade]: [{self.idade}]\n[Fome]: [{self.fome}]\n[Sede]: [{self.sede}]\n[Banho]: [{self.banho}]\n[Saúde]: [{self.saude}]\n[Tédio]: [{self.tedio}]")
        print("-------------------------------")
        print("")
        
    def banho(self, qtd):
        if (self.banho <= 0):
            print(f"{self.nome} não quer tomar banho agora.")
        elif (qtd >= 0 <= 50):
            self.banho += self.banho * (qtd)
            print(f"{self.nome} tomou um banhinho rápido.")
        else:
            self.banho = 100
            print(f"{self.nome} tomou banho e está cheirosinho!")
            
    def beberAgua(self, qtd):
        if (self.sede <= 0):
            print(f"{self.nome} não está com sede.")
        else:
            self.sede -= qtd
            print(f"{self.nome} bebeu {qtd} litros de água.")
            
    def dançar(self, qtd):
        self.tedio -= 20
        self.sede += 10
        
# ----------------------------------------------------   
        
class Pinguim(Tamagoshi):
    def __init__(self, nome, saude, fome, idade, tedio):
        super().__init__(nome, saude, fome, idade, tedio)
        self.peixes = 5
        
    def mostrarInfo():
        print("")
        print(f"------------ {({self.nome}).upper()} ------------")
        print(f"[Idade]: [{self.idade}]\n[Fome]: [{self.fome}]\n[Saúde]: [{self.saude}]\n[Tédio]: [{self.tedio}]\n[IdaEstoque de peixes]: [{self.peixes}]")
        print("-------------------------------")
        print("")
        
    def alimentar(self, qtd):
        if self.peixes > 0:
            super().alimentar(qtd)
        
    def nadar(self):
        self.tedio -= 25
        self.fome += 8
        
    def escorregar_no_gelo(self):
        self.tedio -= 15
        self.fome += 5
        
    def pescar(self, qtd):
        if ((self.peixes <= 10) and (qtd > 0) and (qtd + 10 <= 10)):
            self.peixes += qtd
            print("O estoque de peixes aumentou!")
