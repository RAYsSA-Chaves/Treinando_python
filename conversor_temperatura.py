#Perguntar qual a escala da temperatura:
print("==== Bem-vindo(a) ao seu conversor de temperatura ====\nDigite a letra correspondente à sua opção:")
escala_atual = input("A temperatura atual está na escala: [C] Celsius   [F] Fahrenheit\n>>> ").upper()

#Pedir a temperatura:
temperatura = float(input("Informe a temperatura: "))

#Converter para a escala contrária:
if escala_atual == "F":
    celsius = 5/9 * (temperatura - 32)
    print(f"{temperatura}°F em Celsius é {celsius:.2f}°C")
else:
    fahrenheit = (temperatura * 9/5) + 32
    print(f"{temperatura}°C em Fahrenheit é {fahrenheit:.2f}°F")
