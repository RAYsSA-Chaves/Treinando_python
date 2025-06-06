#Pedir um número ao usuário
n = input("Digite um número interio: ")

#Verificar se é um palíndromo
n_invertido = n[::-1]

#Dizer se é ou não é
if n == n_invertido:
    print(f"{n} é um palíndromo")
else:
    print(f"{n} não é um palíndromo")
