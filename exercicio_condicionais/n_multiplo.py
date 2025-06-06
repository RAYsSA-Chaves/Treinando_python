#Ler dois números inteiros
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

#Dizer se um é múltiplo do outro:
if n1 == n2:
    print("Os números são iguais")
elif (n1 < 0 and n2 > 0) or (n2 < 0 and n1 > 0):
    print("Nenhum número é múltiplo do outro")
elif n1 % n2 == 0:
    print(f"{n1} é múltiplo de {n2}")
elif n2 % n1 == 0:
    print(f"{n2} é múltiplo de {n1}")
else:
    print("Nenhum número é múltiplo do outro")
