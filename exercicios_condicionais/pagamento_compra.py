#Ler preço unitário do produto, quantidade e valor dado pelo cliente:
preco_Un = float(input("Digite o preço unitário do produto: "))
qtd = int(input("Digite a de unidades do produto: "))
valor_pago = float(input("Digite o valor pago em dinheiro: "))

#Verificar se o dinheiro é insuficiente para pagar a compra ou se terá troco:
valor_compra = preco_Un * qtd
if valor_pago < valor_compra:
    valor_faltando = valor_compra - valor_pago
    print(f"O valor total da compra é R${valor_compra:.2f} e você pagou R${valor_pago:.2f}\nFaltam R${valor_faltando:.2f}")
elif valor_pago == valor_compra:
    print(f"O valor total da compra é R${valor_compra:.2f} e você pagou R${valor_pago:.2f}")
else:
    troco = valor_pago - valor_compra
    print(f"O valor total da compra é R${valor_compra:.2f} e você pagou R${valor_pago:.2f}\nTroco de R${troco:.2f}")
