class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, qtd):
        if (self.fome == 0):
            print(f"{self.nome} não está com fome.")
        elif (self.fome - qtd/100 < 0):
            self.fome = 0
        else:
            self.fome -= self.fome * (qtd/100)
            self.sede += 5
            print(f"{self.nome} comeu {qtd} comidinhas.")

    def brincar(self, qtd):
        if (self.tedio - qtd/100 < 0):
            self.tedio = 0
        else:
            self.tedio -= self.tedio * (qtd/100)

    def getHumor(self):
        return ((self.fome + self.tedio)/2)
    
    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or ((self.tedio > 50 and self.tedio <= 60)):
            self.saude -=10
        elif ((self.fome > 60 and self.fome <= 60)) or ((self.tedio > 60 and self.tedio <= 60)):
            self.saude -=30
        elif ((self.fome > 80 and self.fome <= 90)) or ((self.tedio > 80 and self.tedio <= 60)):
            self.saude -=50
        elif (self.fome > 90) or (self.tedio > 90):
            print(f"[{self.nome}] Estou morrendo.......AHHHHHHHHHHHHHHHHHHHHHHH!!!")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            perdeu = True
            print("Seu bichinho morreu T_T")      

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 10
        if (perdeu):
            break
