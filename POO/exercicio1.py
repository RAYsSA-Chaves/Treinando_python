class Livro():
    def __init__(self, titulo: str, autor: str, lançamento: int, paginas: int, genero: str, preço: float, qtd: int, pag_atual = 0):
        self.__titulo = titulo
        self.__autor = autor
        self.__lançamento = lançamento
        self.__paginas = paginas
        lista_generos = ["Romance", "Aventura", "Suspense"]
        if genero in lista_generos:
            self.genero = genero
        else:
            print("Gênero inválido")
        self.pag_atual = pag_atual
        self.__preço = preço
        self.__qtd = qtd

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_lançamento(self):
        return self.__lançamento

    def get_paginas(self):
        return self.__paginas

    def get_preço(self):
        return self.__preço

    def get_qtd(self):
        return self.__qtd

    def set_preço(self):
        novo_preço = float(input("Informe o novo preço do livro: "))
        if novo_preço != self.__preço:
            self.__preço = novo_preço
            print(f"O preço do livro {self.__titulo} foi alterado para {self.__preço}")
        else:
            print(f"Para alterar o preço do livro, escolha um valor diferente do preço atual.")

    def vender_livro(self):
        if self.pag_atual == 0:
            print("Você nem leu o livro ainda. Não o venda!")
        else:
            print(f"O livro {self.__titulo} foi vendido por R${self.__preço}")
            self.__qtd -= 1

    def abrir_livro(self):
        print(f"Você abriu o livro {self.__titulo}.")
        print(f"Informações:\nAutor: {self.__autor}\nGênero: {self.genero}\nAno de lançamento: {self.__lançamento}\nQuantidade de páginas para ler: {self.__paginas}")

    def ler_livro(self):
        paginas_lidas = int(input("Quantas páginas você leu?\n"))
        if self.__paginas < paginas_lidas:
            print(f"Não é possível ler {paginas_lidas} páginas do livro {self.__titulo}, não tem tudo isso de páginas para ler!")
        elif self.__paginas == 0:
            print("Você terminou o livro")
        else:
            self.__paginas -= paginas_lidas
            self.pag_atual = self.__paginas
            print(f"Você leu {paginas_lidas} paginas do livro {self.__titulo}")
            print(f"Páginas restantes: {self.__paginas}")

    def fechar_livro(self):
        print(f"Fechando o livro {self.__titulo}... {self.__paginas} restantes para ler.")

    def __set_qtd(self):
        nova_qtd = int(input("Informe a quantidade atual de livros: "))
        self.__qtd = nova_qtd
        print(f"Quantidade do livro {self.__titulo} atualizada para {self.__qtd}")

    def autorizaçao_edicao(self):
        id = input("Informe o seu ID: ")
        if id == "admin":
            self.__set_qtd()


#Testando:
livro = Livro("A Seleção", "Kiera Cass", 2012, 368, "Romance", 30.00, 2)

livro.abrir_livro()
print()
livro.ler_livro()
print()
livro.ler_livro()
print()
livro.fechar_livro()
print()
print("-----------------")
print(f"Quantidade do livro {livro.get_titulo()}: {livro.get_qtd()}")
print("-----------------")
livro.set_preço()
livro.autorizaçao_edicao()
livro.abrir_livro()
