
# Carrinho contém agregação de Login pois uma contém a outra, mas podem existem independentemente.
from extra import red,green, fim, cyan
class Carrinho: #parte-parte
    
    def __init__(self):
        self.__lista_carrinho = []
    
    def ExibirIntens(self):
        if len(self.__lista_carrinho) == 0:
            print(f'{red}Não há itens no seu carrinho.{fim}')

        else:
            index = 0
            
            for c in self.__lista_carrinho:
                index+=1
                if hasattr(c, 'qtd'): #verifica se a classe/objeto tem atributo
                    print(f'{index} - Nome: {cyan}{c.nome}{fim},  Valor: {cyan}{c.valor_final}{fim}, Quantidade: {cyan}{c.qtd}{fim}')
                        

                else:
                    print(f'{index} - Nome: {cyan}{c.nome}{fim},  Valor: {cyan}{c.valor_final}{fim}')
    
    def verificarTamanho(self):
        return self.__lista_carrinho
                    


    def AdicionarItens(self,item):
        self.__lista_carrinho.append(item)
    

    def RemoverIntens(self,):
        self.ExibirIntens()
        remover = int(input('informe o valo do item:'))
        if remover <=0:
            print('Valor indisponivel')
        else: 
            self.__lista_carrinho.pop(remover-1)
