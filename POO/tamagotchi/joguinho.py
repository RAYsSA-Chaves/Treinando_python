from bichinhos import Dragao, OctoCat, Pinguim

açao = ""  # variável global a ser usada em mais de uma função

# Início - criação do objeto
def start():
    print("""
 ╔════════════════════════════╗
║       🐉 MyPet.py 🐧         ║
 ╚════════════════════════════╝
          
Bem-vindo(a) ao mundo dos bichinhos virtuais! Cuide muito bem do seu!\n
""")
    
    # Escolher o bichinho
    print("Escolha um bichinho para iniciar:")
    bichinho = input("[1] Dragão  [2] OctoCat  [3] Pinguim\n")
    print("")
    # Não permitir opção inválida
    while bichinho not in ("1", "2", "3"):
        print("Opção inválida. Digite o número do bichinho desajado!")
        bichinho = input("[1] Dragão  [2] OctoCat  [3] Pinguim\n")
        print("")
    # Pedir nome do bichinho
    nome_pet = (input("Dê um nome para o seu pet: "))
    
    # Criar o objeto
    if bichinho == "1":
        pet = Dragao(nome_pet)
    elif bichinho == "2":
        pet = OctoCat(nome_pet)
    else:
        pet = Pinguim(nome_pet)

    # Rodar jogo até o bichinho morrer, fugir ou usuário sair
    while ((pet.saude > 0) and (not pet.fugiu) and (açao != "sair")):
        jogo_loop(pet, bichinho)

# --------------------------------------------------

# Loop do jogo que fica pedindo as ações
def jogo_loop(pet, bichinho):
    global açao
    while (açao != "sair"):
            # Sempre exibir as infos do bichinho
            pet.mostrarInfo()
            # Pedir a ação
            print("Cuide do seu bichinho. Escolha a ação desejada:")
            print('(Caso queira encerrar o jogo, digite "sair")\n')
            if (bichinho == "1"):
                açao = input("[1] Alimentar  [2] Brincar  [3] Dar banho  [4] Beber água  [5] Voar  [6] Soltar fogo\n").lower()
            elif (bichinho == "2"):
                açao = input("[1] Alimentar  [2] Brincar  [3] Dar banho  [4] Beber água  [5] Ensinar um truque\n").lower()
            else:
                açao = input("[1] Alimentar  [2] Brincar  [3] Nadar  [4] Pescar\n").lower()

            # Chamar o método e executar a ação
            # Opções iguais entre os três bichinhos
            if (açao == "1"):
                qtd = int(input("Informe a quantidade de comida para dar ao seu pet: "))
                print("")
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.alimentar(qtd)
            elif (açao == "2"):
                qtd = int(input("Informe a quantidade de brincadeira: "))
                print("")
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.brincar(qtd)

            # Opções iguais entre os bichinhos 1 e 2
            elif ((açao == "3") and (bichinho in ("1", "2"))):
                qtd = int(input("Informe a quantidade de banho: "))
                print("")
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.banho(qtd)
            elif ((açao == "4") and (bichinho in ("1", "2"))):
                qtd = int(input("Informe a quantidade de água para dar ao seu pet: "))
                print("")
                qtd_validacao(qtd)
                if (qtd_validacao(qtd)):
                    pet.beberAgua(qtd)

            # Opções individuais dos bichinhos
            elif ((açao == "3") and (bichinho == "3")):
                pet.nadar()
            elif ((açao == "4") and (bichinho == "3")):
                qtd = int(input("Quantos peixes quer tentar pescar?  "))
                print("")
                pet.pescar(qtd)
            elif ((açao == "5") and (bichinho == "1")):
                pet.voar()
            elif ((açao == "5") and (bichinho == "2")):
                pet.aprender_truque()
            elif ((açao == "6") and (bichinho == "1")):
                pet.soltar_fogo()

            # Opção sair
            elif (açao == "sair"):
                print("Saindo...")
            
            # Opção inválida
            else:
                print("Opção inválida.")

            # Sempre passar o tempo
            pet.tempoPassando()

# Não permitir quantidades maiores que 100 (para banho, alimentar, etc)
def qtd_validacao(qtd):
    if qtd > 100:
        print("Quantidade máxima permitida: 100!!!")
        return False
    return True

# --------------------------------------------------

def main():
    start()

# --------------------------------------------------

main()