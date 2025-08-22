class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.fugiu = False
        self.humor = 100
        
     # Não permitir que os atributos sejam maiores que 100 ou menores que 0
    def atualizar_atributo(self, atributo, valor):
        setattr(self, atributo, max(0, min(100, getattr(self, atributo) + valor)))

    def alimentar(self, qtd):
        if self.fome == 0:
            print(f">>>> {self.nome.upper()}: não estou com fome -_-")
        else:
            print(f">>>> {self.nome.upper()}: Nhac nhac nhac")
            self.atualizar_atributo("fome", -qtd / 10)
            self.atualizar_atributo("saude", 5)
            self.atualizar_atributo("humor", 2)

    def brincar(self, qtd):
        if self.humor < 20:
            print(f">>>> {self.nome} está de mau humor e não quer brincar!")
            self.atualizar_atributo("tedio", 5)
        else:
            print(f">>>> {self.nome} brincou e se divertiu!")
            self.atualizar_atributo("tedio", -qtd / 10)
            self.atualizar_atributo("humor", 5)
            self.atualizar_atributo("fome", 5)
            if hasattr(self, "sede"):
                self.atualizar_atributo("sede", 5)

    def getHumor(self):
        calculo_humor = self.humor - ((self.fome + self.tedio) / 2)
        self.humor = max(0, min(100, calculo_humor))
    
    def vida(self):
        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.atualizar_atributo("saude", -10)
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
             self.atualizar_atributo("saude", -30)
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
             self.atualizar_atributo("saude", -35)
        elif (90 < self.fome <= 99) or (90 < self.tedio <= 99):
            print(f">>>> {self.nome.upper()}: Estou morrendo.......AHHHHHHHHHHHHHHHHHHHHHHH!!!")
            self.atualizar_atributo("saude", -40)
        elif (self.fome >= 100) or (self.tedio >= 100):
            self.saude = 0
            print(">>>> Seu bichinho morreu T_T")  
            
        if (self.saude <= 0):
              print(">>>> Seu bichinho morreu T_T") 

    def tempoPassando(self):
        self.idade += 0.2
        self.atualizar_atributo("tedio", 2)
        self.atualizar_atributo("fome", 2)
        if hasattr(self, "sede"):
            self.atualizar_atributo("sede", 2)
        print(f">>>> Um tempo se passou e {self.nome} deu uma crescidinha!")

    def fugir(self):
        # padrão: não foge
        return False
