from extra import fim, green, red
from abc import ABC
from comida import Comida

class SistemaCadastro(ABC):# arrumado
#commit:
  def __init__(self, nome: str, senha: str, email: str):
    self.__nome = nome
    self.__email = email
    self.__senha = senha

  def Cadastro(self, lista: list ,objeto: object) -> None:
    lista.append(objeto)
    print(f'{green}Cadastro feito com sucesso{fim}')
    
  def getNome(self) -> str: 
    return self.__nome
  def getSenha(self) -> str:
    return self.__senha
  

# CadastroAluno contém herança de Cadastro, pois herdam vários atributos e métodos.
#commit: cadastrando aluno no cadatro
class CadastroAluno(SistemaCadastro): #subclasse

  def __init__(self, nome, senha, email):
    super().__init__(nome, senha, email)
    

  def getNome(self):
    return super().getNome()

  def getSenha(self):
    return super().getSenha()

  def Cadastro(self, lista,objeto):
    super().Cadastro(lista,objeto)


# CadastroAdm contém herança de Cadastro, pois herdam vários atributos e métodos
#commit: Cadastrando o aluno no cadastro no sistema 
class CadastroAdm(SistemaCadastro): #subclasse

  def __init__(self, nome, senha, email,cod = '101'): # cod é a verificação do ADM
    super().__init__(nome, senha, email)
    self.__cod = cod


  def getSenha(self):
    return super().getSenha() 
  
  def getNome(self):
    return super().getNome() 

  def Cadastro(self, lista,objeto):

    cod_adm = input('Informa o numero de ADM: ')
    if cod_adm == self.__cod:
      super().Cadastro(lista,objeto)
    else:
      print(f'{red}Conta não cadastrada no banco de dados{fim}')
    
  def alterar_Valor(self, item: object, Novo_valor):
    item.set_valor(Novo_valor)
