from abc import ABC
from extra import fim, green, red


# SistemaLogin contém agregação de Carrinho pois uma contém a outra, mas podem existem independentemente.
class Sistemalogin(ABC): #superclasse,  parte-todo


  def __init__(self, nome: str, senha: str, status: bool):
    self.__nome = nome
    self.__senha = senha
    self.status = status
   
  def verificar(self, lista: list):  # mudar variavel 'lista' pela de vocês na hora da subclasse
    try:
      for c in lista:
        if c.getNome() == self.__nome and c.getSenha() == self.__senha:
          
          self.status = True

        else: 
          pass 

    except:
      print(f'{red}Não possue contas no banco dados {fim}')

#LoginAluno contém herança de Login pois herdam vários atributos e métodos
class LoginAluno(Sistemalogin):
  def __init__(self, nome, senha,status):
    super().__init__(nome, senha,status)
  

  def verificar(self, lista):
    super().verificar(lista)

# LoginAdm contém herança de Login pois herdam vários atributos e métodos  
class LoginAdm(Sistemalogin):#Arrumado
  def __init__(self, nome, senha,status,cod = '101'):
    super().__init__(nome, senha,status)
    self.__cod = cod
  

  def verificar(self, lista) -> None:
    cod_adm = input('Informe o cod de ADM:')

    if cod_adm == self.__cod:
      super().verificar(lista)

    else:
      print(f'{red}Codigo invalido{fim}')
  

