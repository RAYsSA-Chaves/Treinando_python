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
        self.temperamento += 2
        
    def tomarBanho(self, qtd):
        if (self.banho == 100):
            print(f">>>> {self.nome.upper()}: Não quero tomar banho agora -_-")
            self.tedio += 5
            self.temperamento += 10
        elif (qtd + self.banho <= 100):
            self.banho += qtd/10
            print(f">>>> {self.nome} tomou um banhinho rápido.")
        else:
            self.banho = 100
            print(f">>>> {self.nome} tomou banho e está cheirosinho!")

    def beberAgua(self, qtd):
        if (self.sede == 0):
            print(f">>>> {self.nome.upper()}: Não estou com sede -_-")
            self.tedio += 5
            self.temperamento += 10
        elif (self.sede - qtd < 0):
            self.sede = 0
            print(f">>>> {self.nome.upper()}: Glub glub glub")
        else:
            self.sede -= qtd
            print(f">>>> {self.nome.upper()}: Glub glub glub")

    def voar(self):
        if (self.tedio - 10 < 0):
            self.tedio = 0
        else:
            self.tedio -= 10
        if (self.fome + 5 > 100):
            self.fome = 100
        else:
            self.fome += 5
        if (self.sede + 5 > 100):
            self.sede = 100
        else:
            self.sede += 5
        if (self.humor + 5 < 100):
                self.humor += 5
        else:
            self.humor = 100
        print(f">>>> {self.nome} deu um rolê pelo céu e está mais feliz agora :D")

    def soltar_fogo(self):
        if (self.tedio - 20 < 0):
            self.tedio = 0
        else:
            self.tedio -= 20
        if (self.temperamento - 20 < 0):
            self.temperamento = 0
        else:
            self.temperamento -= 20
        if (self.humor + 10 < 100):
                self.humor += 10
        else:
            self.humor = 100
        print(f">>>> {self.nome} cuspiu fogo por todos os lados e está mais calmo agora ^_^")
    
    def fugir(self):
        if (self.temperamento > 99):
            print(f">>>> {self.nome} ficou tão revoltado que fugiu T_T")
            self.fugiu = True

    def tempoPassando(self):
        super().tempoPassando()

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
        if (self.banho == 100):
            print(f">>>> {self.nome.upper()}: Não quero tomar banho agora -_-")
            self.tedio += 5
        elif (qtd + self.banho <= 100):
            self.banho += (qtd/10)
            print(f">>>> {self.nome} tomou um banhinho rápido.")
        else:
            self.banho = 100
            print(f">>>> {self.nome} tomou banho e está cheirosinho!")
    
    def beberAgua(self, qtd):
        if (self.sede == 0):
            print(f">>>> {self.nome.upper()}: Não estou com sede.")
            self.tedio += 5
        elif (self.sede - qtd < 0):
            self.sede = 0
            print(f">>>> {self.nome.upper()}: Glub glub glub")
        else:
            self.sede -= qtd/5
            print(f">>>> {self.nome.upper()}: Glub glub glub")
            
    def aprender_truque(self):
        if self.humor < 20:
            print(f">>>> {self.nome} está de mau humor e não quer aprender um truque novo!")
            self.tedio += 5
        elif (self.tedio - 10 < 0):
            self.tedio = 0
            if (self.sede + 10 > 100):
                self.sede = 100
            else:
                self.sede += 10 
            if (self.humor + 5 < 100):
                self.humor += 5
            else:
                self.humor = 100
            print(f">>>> {self.nome} aprendeu um novo truque!")
        else:
            self.tedio -= 10
            if (self.sede + 10 > 100):
                self.sede = 100
            else:
                self.sede += 10 
            if (self.humor + 5 < 100):
                self.humor += 5
            else:
                self.humor = 100
            print(f">>>> {self.nome} aprendeu um novo truque!")
        
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
                if (self.fome - qtd < 0):
                    self.fome = 0
                    print(f">>>> {self.nome.upper()}: Nhac nhac nhac")
                else:
                    self.fome -= qtd
                    print(f">>>> {self.nome.upper()}: Nhac nhac nhac")
            else:
                print(">>>> Quantidade de peixes insuficiente.")
        else:
            print(">>>> Os peixes acabaram :(")
        
    def nadar(self):
        if (self.tedio - 25 < 0):
            self.tedio = 0
        else:
            self.tedio -= 25
        if (self.fome + 8 > 100):
            self.fome = 100
        else:
            self.fome += 8 
        if (self.humor + 5 < 100):
            self.humor += 5
        else:
            self.humor = 100
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
