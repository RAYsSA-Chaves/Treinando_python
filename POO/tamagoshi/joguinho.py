from bichinhos import Dragao, OctoCat, Pinguim

def qtd_validacao(qtd):
    if qtd > 100:
        print("Quantidade máxima permitida: 100!!!")
        return False
    return True

def jogo_loop(pet, bichinho):
    açao = ""
    while (açao != "sair"):
            pet.mostrarInfo()
            print("Cuide do seu bichinho. Escolha a ação desejada:")
            print('(Caso queira encerrar o jogo, digite "sair")')
            if (bichinho == "1"):
                açao = input("[1] Alimentar  [2] Brincar  [3] Dar banho  [4] Beber água  [5] Voar  [6] Soltar fogo\n").lower()
            elif (bichinho == "2"):
                açao = input("[1] Alimentar  [2] Brincar  [3] Dar banho  [4] Beber água  [5] Ensinar um truque\n").lower()
            else:
                açao = input("[1] Alimentar  [2] Brincar  [3] Nadar  [4] Pescar\n").lower()

            # opções iguais entre os três
            if (açao == "1"):
                qtd = int(input("Informe a quantidade de comida para dar ao seu pet: "))
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.alimentar(qtd)
            elif (açao == "2"):
                qtd = int(input("Informe a quantidade de brincadeira: "))
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.brincar(qtd)

            # opções iguais entre os bichinhos 1 e 2
            elif ((açao == "3") and (bichinho in ("1", "2"))):
                qtd = int(input("Informe a quantidade de banho: "))
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.banho(qtd)
            elif ((açao == "4") and (bichinho in ("1", "2"))):
                qtd = int(input("Informe a quantidade de água para dar ao seu pet: "))
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.beberAgua(qtd)

            # opções diferentes para todos
            elif ((açao == "3") and (bichinho == "3")):
                pet.nadar()
            elif ((açao == "4") and (bichinho == "3")):
                qtd = int(input("Quantos peixes quer tentar pescar?  "))
                pet.pescar(qtd)
            elif ((açao == "5") and (bichinho == "1")):
                pet.voar()
            elif ((açao == "5") and (bichinho == "2")):
                pet.aprender_truque()
            elif ((açao == "6") and (bichinho == "1")):
                pet.soltar_fogo()
            
            # opção inválida
            else:
                print("Opção inválida.")

            # sempre passar o tempo
            pet.tempoPassando()

def main():
    print("""
 ╔════════════════════════════╗
║       🐉 MyPet.py 🐧        ║
 ╚════════════════════════════╝
Bem-vindo(a) ao mundo dos bichinhos virtuais! Cuide muito do seu!\n
""")
    
    print("Escolha um bichinho para iniciar:")
    bichinho = input("[1] Dragão  [2] OctoCat  [3] Pinguim")
    print("")
    while bichinho not in ("1", "2", "3"):
        print("Opção inválida. Digite o número do bichinho desajado!\n")
        bichinho = int(input("[1] Dragão  [2] OctoCat  [3] Pinguim"))
        print("")
    nome_pet = input("Dê um nome para o seu pet: ")
    
    if bichinho == "1":
        pet = Dragao(nome_pet)
    elif bichinho == "2":
        pet = OctoCat(nome_pet)
    else:
        pet = Pinguim(nome_pet)

    while pet.saude > 0 and not pet.fugiu:
        jogo_loop(pet, bichinho)