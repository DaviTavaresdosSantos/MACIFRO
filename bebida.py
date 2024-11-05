# Bebida contém agregação de Carrinho pois uma contém a outra, mas podem existem independentemente.
class Bebida:
    def __init__(self,nome,descricao,valor,quantidade,ml):
        self.nome = nome
        self.descricao = descricao
        self.__valor = valor
        self.qtd = quantidade
        self.ml = ml
        self.valor_final = self.__valor * self.qtd

    def get_valor(self):
        return self.__valor

    def set_valor(self, NovoValor):
        self.__valor = NovoValor

    def atualizar(self):
        self.valor_final = self.__valor * self.qtd

def exibir_detalhes (self):
    print(f"Bebida: {self.nome}")
    print(f"descricao:{self.descricao}")
    print(f"valor: R${self.__valor:.2f}")
    print(f"quantidade em estoque: {self.qtd}")
    print(f"volume:{self.ml} ml")



