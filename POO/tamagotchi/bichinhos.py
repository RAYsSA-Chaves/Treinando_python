from tamagotchi import Tamagotchi

class Dragao(Tamagotchi):
    def __init__(self, nome):
        super().__init__(nome)
        self.banho = 50
        self.sede = 0
        self.saude = 200
        self.temperamento = 0

    def mostrarInfo(self):
        super().getHumor()
        print("")
        print(f"══════════════════ {self.nome.upper()} ══════════════════")
        print(f"[Idade]: [{self.idade}]\n[Fome]: [{self.fome}]\n[Sede]: [{self.sede}]\n[Banho]: [{self.banho}]\n[Saúde]: [{self.saude}]\n[Tédio]: [{self.tedio}]\n[Temperamento]: [{self.temperamento}]\n[Humor]: [{self.humor}]")
        print("════════════════════════════════════════════════")
        print("")
        self.atualizar_atributo("temperamento", 2)
        
    def tomarBanho(self, qtd):
        if (self.banho == 100):
            print(f">>>> {self.nome.upper()}: Não quero tomar banho agora -_-")
            self.atualizar_atributo("tedio", 5)
            self.atualizar_atributo("temperamento", 10)
        else:
            self.atualizar_atributo("banho", qtd / 5)
            print(f">>>> {self.nome} tomou banho.")

    def beberAgua(self, qtd):
        if (self.sede == 0):
            print(f">>>> {self.nome.upper()}: Não estou com sede -_-")
            self.atualizar_atributo("tedio", 5)
            self.atualizar_atributo("temperamento", 10)
        else:
            self.atualizar_atributo("sede", -qtd / 5)
            print(f">>>> {self.nome.upper()}: Glub glub glub")

    def voar(self):
        print(f">>>> {self.nome} deu um rolê pelo céu e está mais feliz agora :D")
        self.atualizar_atributo("tedio", -10)
        self.atualizar_atributo("fome", 8)
        self.atualizar_atributo("sede", 8)
        self.atualizar_atributo("humor", 5)

    def soltar_fogo(self):
        print(f">>>> {self.nome} cuspiu fogo por todos os lados e está mais calmo agora ^_^")
        self.atualizar_atributo("tedio", -20)
        self.atualizar_atributo("temperamento", -20)
        self.atualizar_atributo("humor", 10)
        self.atualizar_atributo("fome", 5)
        self.atualizar_atributo("sede", 5)
    
    def fugir(self):
        if (self.temperamento > 99):
            print(f"\n>>>> {self.nome} ficou tão revoltado que fugiu T_T")
            self.fugiu = True

# ----------------------------------------------------

class OctoCat(Tamagotchi):
    def __init__(self, nome):
        super().__init__(nome)
        self.banho = 50
        self.sede = 0
        
    def mostrarInfo(self):
        super().getHumor()
        print("")
        print(f"══════════════════ {self.nome.upper()} ══════════════════")
        print(f"[Idade]: [{self.idade}]\n[Fome]: [{self.fome}]\n[Sede]: [{self.sede}]\n[Banho]: [{self.banho}]\n[Saúde]: [{self.saude}]\n[Tédio]: [{self.tedio}]\n[Humor]: [{self.humor}]")
        print("════════════════════════════════════════════════")
        print("")
        
    def tomarBanho(self, qtd):
        if (self.banho >= 100):
            print(f">>>> {self.nome.upper()}: Não quero tomar banho agora -_-")
            self.atualizar_atributo("tedio", 5)
        else:
            self.atualizar_atributo("banho", qtd / 5)
            print(f">>>> {self.nome} tomou banho.")
        
    def beberAgua(self, qtd):
        if (self.sede == 0):
            print(f">>>> {self.nome.upper()}: Não estou com sede.")
            self.atualizar_atributo("tedio", 5)
        else:
            self.atualizar_atributo("sede", -qtd / 5)
            print(f">>>> {self.nome.upper()}: Glub glub glub")
            
    def aprender_truque(self):
        if self.humor < 20:
            print(f">>>> {self.nome} está de mau humor e não quer aprender um truque novo!")
            self.atualizar_atributo("tedio", 5)
        else:
            self.atualizar_atributo("tedio", -10)
            self.atualizar_atributo("sede", 10)
            self.atualizar_atributo("fome", 5)
            self.atualizar_atributo("humor", 5)
            
# ----------------------------------------------------   
        
class Pinguim(Tamagotchi):
    def __init__(self, nome):
        super().__init__(nome)
        self.peixes = 5
        
    def mostrarInfo(self):
        super().getHumor()
        print("")
        print(f"══════════════════ {self.nome.upper()} ══════════════════")
        print(f"[Idade]: [{self.idade}]\n[Fome]: [{self.fome}]\n[Saúde]: [{self.saude}]\n[Tédio]: [{self.tedio}]\n[Estoque de peixes]: [{self.peixes}]\n[Humor]: [{self.humor}]")
        print("════════════════════════════════════════════════")
        print("")
        
    def alimentar(self, qtd):
        if (self.fome == 0):
            print(f">>>> {self.nome.upper()}: não estou com fome -_-")
        elif (self.peixes > 0):
            if ((qtd <= self.peixes) and (qtd > 0)):
                self.peixes -= qtd
                self.atualizar_atributo("fome", -qtd * 5)
                self.atualizar_atributo("saude", 5)
                self.atualizar_atributo("humor", 3)
        else:
            print(">>>> Quantidade de peixes insuficiente.")
        
    def nadar(self):
        self.atualizar_atributo("tedio", -25)
        self.atualizar_atributo("fome", 10)
        self.atualizar_atributo("humor", 5)
        print(f">>>> {self.nome} nadou e está mais feliz agora :D")
        
    def pescar(self, qtd):
        if ((self.peixes < 10) and (qtd > 0) and (self.peixes + qtd <= 10)):
            self.peixes += qtd
            print(">>>> O estoque de peixes aumentou!")
        elif (self.peixes >= 10):
            print(">>>> O estoque de peixes está cheio!")
        elif (self.peixes + qtd > 10):
            peixes_fugidos = self.peixes + qtd - 10 
            self.peixes += qtd - peixes_fugidos
            print(f">>>> Não é possível guardar mais de 10 peixes no estoque. {peixes_fugidos} peixes fugiram.")
        else:
            print(">>>> Quantidade de peixes insuficiente para pescar.")
