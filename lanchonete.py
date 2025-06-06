#Pedir o código do produto desejado:
print("===== BEM-VONDO(A) À LANCHONETE DO DAN ====\nDigite o código do produto que deseja:")
codigo = int(input("[1] Salgado assado   [2] Coca-cola 200ml   [3] Misto quente   [4] Lanche Classic   [5] Cachorro-quente\n>>> "))

#Perguntar a quantidade:
qtd = int(input("Qual a quantidade desejada do produto? "))

#Calcular:
if codigo == 1:
    total = qtd * 5
    produto = "salgado assado"
elif codigo == 2:
    total = qtd * 3.5
    produto = "coca-cola 200ml"
elif codigo == 3:
    total = qtd * 4.8
    produto = "misto quente"
elif codigo == 4:
    total = qtd * 8.9
    produto = "lanche Classic"
else:
    total = qtd * 7.32
    produto = "cachorro-quente"

#Exibir o valor total a ser pago:
print(f"Você pediu {qtd} {produto}. Valor total do pedido: R${total:.2f}")
