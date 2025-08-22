class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.fugiu = False
        self.humor = 100

    def alimentar(self, qtd):
        if (self.fome == 0):
            print(f">>>> {self.nome.upper()}: não estou com fome -_-")
        elif (self.fome - qtd/20 < 0):
            self.fome = 0
            print(f">>>> {self.nome.upper()}: Nhac nhac nhac")
        else:
            self.fome -= qtd/20
            print(f">>>> {self.nome.upper()}: Nhac nhac nhac")

    def brincar(self, qtd):
        if self.humor < 20:
            print(f">>>> {self.nome} está de mau humor e não quer brincar!")
            self.tedio += 5
        elif (self.tedio - qtd/20 < 0):
            self.tedio = 0
            if (self.humor + 2 < 100):
                self.humor += 2
            else:
                self.humor = 100
            print(f">>>> {self.nome} brincou e se divertiu!")
        else:
            self.tedio -= self.tedio * (qtd/20)
            self.humor += 2
            print(f">>>> {self.nome} brincou e se divertiu!")

    def getHumor(self):
        if ((self.humor - ((self.fome + self.tedio)/2)) < 0):
            self.humor = 0
        else:
            self.humor -= (self.fome + self.tedio)/2
    
    def vida(self):
        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude -= 10
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude -= 30
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude -= 5
        elif (90 < self.fome <= 99) or (90 < self.tedio <= 99):
            print(f">>>> {self.nome.upper()}: Estou morrendo.......AHHHHHHHHHHHHHHHHHHHHHHH!!!")
        elif (self.fome >= 100) or (self.tedio >= 100):
            self.saude = 0
            print(">>>> Seu bichinho morreu T_T")    

    def tempoPassando(self):
        self.idade += 0.2
        self.tedio += 2
        self.fome += 2
        print(f">>>> Um tempo se passou e {self.nome} deu uma crescidinha!")

    def fugir(self):
        # padrão: não foge
        return False
