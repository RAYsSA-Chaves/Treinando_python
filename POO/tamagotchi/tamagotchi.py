class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.fugiu = False

    def alimentar(self, qtd):
        if (self.fome == 0):
            print(f"{self.nome} não está com fome.")
        elif (self.fome - qtd/100 < 0):
            self.fome = 0
        else:
            self.fome -= self.fome * (qtd/100)
            print(f"{self.nome} comeu {qtd} comidinhas.")

    def brincar(self, qtd):
        if self.getHumor() > 80:
            print(f"{self.nome} está de mau humor e não quer brincar!")
        elif (self.tedio - qtd/100 < 0):
            self.tedio = 0
            print(f"{self.nome} brincou e se divertiu!")
        else:
            self.tedio -= self.tedio * (qtd/100)
            print(f"{self.nome} brincou e se divertiu!")

    def getHumor(self):
        return ((self.fome + self.tedio)/2)
    
    def vida(self):
        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude -= 10
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude -= 30
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            print(f"[{self.nome}] Estou morrendo.......AHHHHHHHHHHHHHHHHHHHHHHH!!!")
        if (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu T_T")     

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 2.5
