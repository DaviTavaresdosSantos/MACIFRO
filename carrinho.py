
# Carrinho contém agregação de Login pois uma contém a outra, mas podem existem independentemente.
class Carrinho: #parte-parte
    
    def __init__(self) -> None:
        self.__lista_carrinho = []
    
    def ExibirIntens(self):
        if len(self.__lista_carrinho) == 0:
            print('Não há itens no seu carrinho.')

        else:
            print("Nome: valor(Final): quantidade:")
            index = 0
            
            for c in self.__lista_carrinho:
                index+=1
                if hasattr(c, 'qtd'): #verifica se a classe/objeto tem atributo
                    print(f'{index} - {c.nome} : {c.valor_final} : {c.qtd}')
                        

                else:
                    print(f'{index} - {c.nome} : {c.valor_final}')
                    


    def AdicionarItens(self,item):
        self.__lista_carrinho.append(item)
    

    def RemoverIntens(self,):
        self.ExibirIntens()
        remover = int(input('informe o valo do item:'))
        if remover <=0:
            print('Valor indisponivel')
        else: 
            self.__lista_carrinho.pop(remover-1)
