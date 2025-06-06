#Ler dois números
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um novo número: "))

#Comparar para achar o maior
if n1 > n2:
    print(f"{n1} é maior")
elif n2 > n1:
    print(f"{n2} é maior")
else:
    print("Os números são iguais")
