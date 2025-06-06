class Livro():
    def __init__(self, titulo: str, autor: str, lançamento: int, paginas: int, genero: str, pag_atual = 0):
        self.titulo = titulo
        self.autor = autor
        self.lançamento = lançamento
        self.paginas = paginas
        lista_generos = ["Romance", "Aventura", "Suspense"]
        if genero in lista_generos:
            self.genero = genero
        else:
            print("Gênero inválido")
        self.pag_atual = pag_atual

    def abrir_livro(self):
        print(f"Você abriu o livro {self.titulo}.")
        print(f"Informações:\nAutor: {self.autor}\nGênero: {self.genero}\nAno de lançamento: {self.lançamento}\nQuantidade de páginas para ler: {self.paginas}")

    def ler_livro(self, paginas_lidas: int):
        if self.paginas < paginas_lidas:
            print(f"Não é possível ler {paginas_lidas} páginas do livro {self.titulo}, não tem tudo isso de páginas para ler!")
        elif self.paginas == 0:
            print("Você terminou o livro")
        else:
            self.paginas -= paginas_lidas
            self.pag_atual = self.paginas
            print(f"Você leu {paginas_lidas} paginas do livro {self.titulo}")
            print(f"Páginas restantes: {self.paginas}")

    def fechar_livro(self):
        print(f"Fechando o livro {self.titulo}... {self.paginas} restantes para ler.")

    def vender_livro(self, valor: float):
        if self.pag_atual == 0:
            print("Você nem leu o livro ainda. Não o venda!")
        else:
            print(f"O livro {self.titulo} foi vendido por R${valor:.2f}")

livro1 = Livro("A Seleção", "Kiera Cass", 2012, 368, "Romance")
livro2 = Livro("O Homem de Giz", "C. J. Tudor", 2018, 272, "Suspense")

livro1.abrir_livro()
print()
livro1.ler_livro(100)
print()
livro1.ler_livro(100)
print()
livro1.fechar_livro()
print()
livro1.abrir_livro()
print()
livro1.ler_livro(200)

print("-----------------")

livro2.abrir_livro()
print()
livro2.vender_livro(40)
