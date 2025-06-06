#Ler três números inteiros:
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite mais um número inteiro: "))
n3 = int(input("Digite mais um número inteio: "))

#Achar o menor e exibir:
if n1 == n2 == n3:
    print(f"Os números são iguais. O menor número  é {n2}")
elif n1 <= n2 <= n3:
    print(f"Números escolhidos: {n1}, {n2}, {n3} e o menor número é {n1}")
elif n2 <= n1 <= n3:
    print(f"Números escolhidos: {n1}, {n2}, {n3} e o menor número é {n2}")
else:
    print(f"Números escolhidos: {n1}, {n2}, {n3} e o menor número é {n3}")
