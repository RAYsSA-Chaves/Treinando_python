#Cadastrar 3 usuários
print("----------BEM-VINDO(A)----------")
print("Cadastre-se\n")

print("Usuário 1")
usuario1 = input("Usuário: ")
senha1 = input("Senha: ")
resp1 = input("Responda a pergunta de recuperação de senha: Qual é a sua comida preferida? ")
print()

print("Usuário 2")
usuario2 = input("Usuário: ")
senha2 = input("Senha: ")
resp2 = input("Responda a pergunta de recuperação de senha: Qual é a sua comida favorita? ")
print()

print("Usuário 3")
usuario3 = input("Usuário: ")
senha3 = input("Senha: ")
resp3 = input("Responda a pergunta de recuperação de senha: Qual é a sua comida favorita? ")
print()

#Menu
print("----------MENU----------")
print("Digite a opção numérica correspondente à ação desejada:")
print("[1] Login\n[2] Esqueci a senha\n[3] Sair")
opçao = input(">>> ")
print()

#Login
if opçao == "1":
    print("----------BEM-VINDO(A) DE VOLTA----------")
    print("Entre na sua conta\n")
    tentativa_usuario = input("Usuário: ")
    tentativa_senha = input("Senha: ")
    print()
    #Usuário 1
    if tentativa_usuario == usuario1:
        if tentativa_senha == senha1:
            print(f"Acesso permitido.\nBem-vindo(a), {usuario1}.")
        else:
            print("Senha incorreta, tente novamente (2 tentativas restantes)")
            tentativa_senha = input("Senha: ")
            print()
            if tentativa_senha == senha1:
                print(f"Acesso permitido.\nBem-vindo(a), {usuario1}.")
            else:
                print("Senha incorreta, tente novamente (1 tentativa restante)")
                tentativa_senha = input("Senha: ")
                print()
                if tentativa_senha == senha1:
                    print(f"Acesso permitido.\nBem-vindo(a), {usuario1}.")
                else:
                    print("Senha incorreta, usuário bloqueado. Reinicie o sistema.")
    #Usuário 2
    elif tentativa_usuario == usuario2:
        if tentativa_senha == senha2:
            print(f"Acesso permitido.\nBem-vindo(a), {usuario2}.")
        else:
            print("Senha incorreta, tente novamente (2 tentativas restantes)\n")
            tentativa_senha = input("Senha: ")
            print()
            if tentativa_senha == senha2:
                print(f"Acesso permitido.\nBem-vindo(a), {usuario2}.")
            else:
                print("Senha incorreta, tente novamente (1 tentativa restante)\n")
                tentativa_senha = input("Senha: ")
                print()
                if tentativa_senha == senha2:
                   print(f"Acesso permitido.\nBem-vindo(a), {usuario2}.")
                else:
                   print("Senha incorreta, usuário bloqueado. Reinicie o sistema.")
    #Usuário 3
    elif tentativa_usuario == usuario3:
        if tentativa_senha == senha3:
            print(f"Acesso permitido.\nBem-vindo(a), {usuario3}.")
        else:
            print("Senha incorreta, tente novamente (2 tentativas restantes)\n")
            tentativa_senha = input("Senha: ")
            print()
            if tentativa_senha == senha3:
                print(f"Acesso permitido.\nBem-vindo(a), {usuario3}.")
            else:
                print("Senha incorreta, tente novamente (1 tentativa restante)\n")
                tentativa_senha = input("Senha: ")
                print()
                if tentativa_senha == senha3:
                    print(f"Acesso permitido.\nBem-vindo(a), {usuario3}.")
                else:
                    print("Senha incorreta, usuário bloqueado. Reinicie o sistema.")
    #Usuário inexistente
    else:
        print("Usuário não cadastrado. Acesso negado.")
#Recuperar senha
elif opçao == "2":
    print("----------RECUPERAÇÃO DE SENHA----------")
    conta = input("De qual conta deseja recuperar a senha? ")
    print()
    #Usuário 1
    if conta == usuario1:
        tentativa_resp = input("Responda a pergunta secreta para recuperar a senha: Qual a sua comida preferida? ")
        print()
        if tentativa_resp == resp1:
            print(f"Resposta correta.\nSenha: {senha1}")
        else:
            print(f"Resposta incorreta.")
    #Usuário 2
    elif conta == usuario2:
        tentativa_resp = input("Responda a pergunta secreta para recuperar a senha: Qual a sua comida preferida? ")
        print()
        if tentativa_resp == resp2:
            print(f"Resposta correta.\nSenha: {senha2}")
        else:
            print("Resposta incorreta.")
    #Usuário 3
    elif conta == usuario3:
        tentativa_resp = input("Responda a pergunta secreta para recuperar a senha: Qual a sua comida preferida? ")
        print()
        if tentativa_resp == resp3:
            print(f"Resposta correta.\nSenha: {senha3}")
        else:
            print("Resposta incorreta.")
    #Usuário inexistente
    else:
        print("Usuário não cadastrado.")
#Sair
else:
  print("Você saiu.")
  
