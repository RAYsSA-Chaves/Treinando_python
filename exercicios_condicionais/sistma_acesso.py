#Definindo usuário, senha, código de verificação e primeira tentativa
usuario_certo = "rayssa"
senha_certa = "1234"
codigo_certo = "999"
tentativa = 1

#Solicitar usuário e senha
print("--------------LOGIN--------------")
usuario = input("Usuário: ")
senha = input("Senha: ")
print()

#Verificando usuário digitado
if usuario != usuario_certo:
    print("Usuário não reconhecido. Acesso negado.")
else:
    #Verificando a senha digitada
    if senha != senha_certa:
        print(f"Senha incorreta. Tente novamente ({3 - tentativa} tentativas restantes)\n")
        senha = input(("Senha: "))
        print("--------------------")
        tentativa +=1
        if senha != senha_certa:
            print(f"Senha incorreta. Tente novamente ({3 - tentativa} tentativa restante)")
            print("DICA: Sua senha é composta apenas por números consecutivos!\n")
            senha = input(("Senha: "))
            print("--------------------")
            if senha != senha_certa:
                print(f"Senha inválida. Sistema bloqueado. Contate o administrador.")
    #Se acertou a senha, pedir código de verificação e validar
    else:
        cod = input("Digite o código de verificação: ")
        print()
        if cod != codigo_certo:
            print("Código inválido. Acesso negado.")
        else:
           #Verificar o horário do acesso
           hora = int(input("Digite a hora em que está acessando: "))
           print()
           if 8 <= hora <= 18:
               print("--------------------")
               print(f"Acesso permitido. Bem-vindo(a), {usuario}!")
           else:
               print("Acesso negado. Horário permitido somente entre 8h e 18h.")
