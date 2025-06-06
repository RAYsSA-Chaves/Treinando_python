#Ler valores de x e y:
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

#Determinar qual o quadrante da coordenada ou se está na origem ou sobre um dos eixos:
if x == 0 and y == 0:
    print("A coordenada está na origem")
elif x == 0 and (y<0 or y>0):
    print("A coordenada está sobre o Eixo Y")
elif (x>0 or x<0) and y == 0:
    print("A coordenada está sobre o Eixo X")
elif x>0 and y>0:
    print("A coordenada está no quadrante Q1")
elif x<0 and y>0:
    print("A coordenada está no quadrante Q2")
elif x<0 and y<0:
    print("A coordenada está no quadrante Q3")
else:
    print("A coordenada está no quadrante Q4")
