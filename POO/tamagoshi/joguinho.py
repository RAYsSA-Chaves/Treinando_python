from tamagoshi import Tamagoshi

class Dragao(Tamagoshi):
    def __init__(self, nome, saude):
        super().__init__(nome, saude)
        self.banho = 0
        self.sede = 0
        self.saude = 200

    def alimentar(self, qtd):
        if (self.fome == 0):
            print(f"{self.nome} não está com fome.")
        elif (qtd >= 0) and (qtd <= 100):
            self.fome -= self.fome * (qtd/50)
            print(f"{self.nome} comeu {qtd} comidinhas.")
            super().mostrarInfo()
        
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

class Pou(Tamagoshi):
    def __init__(self, nome, banho):

        super().__init__(nome)
