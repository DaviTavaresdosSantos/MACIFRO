'''Informática 2A, POO
Integrantes:  Davi Tavares dos Santos, WILLIAM CAVALCANTE DAMACENO, Júlia Marcelly Braga Belchior, João Vitor Silva Maciel, Layra Vitória Mota Leal'''

from classe import LoginAdm, CadastroAluno, CadastroAdm,LoginAluno
from extra import red,fim, clear



ADM_conta = []
Aluno_conta = [] # Exemplo de conta


def cadastrar(subclasse,lista):

  nome = input('Digite seu nome:')
  senha = input('Digite seu senha:')
  email = input('Digite seu email:')
  objeto_acessor = subclasse(nome, senha, email)
  objeto_acessor.Cadastro(lista,objeto_acessor)
  
def logar(subclasse,lista):  

  global objeto_acessor
  
  nome = input('Informe seu nome:')
  senha = input('Informe sua senha:')
  objeto_acessor = subclasse(nome, senha)
  objeto_acessor.verificar(lista)




def menu():
    global objeto_acessor,ADM_conta,Aluno_conta,clear

    while True:
    
        print(f'''
{'========== MENU =========='}
Olá, seja bem vindo ao MecIFRO, o que você deseja fazer?
1. Cadastrar 
2. login
''')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            clear()
            while True:
              print(f'''
{'========== CADASTRO =========='}
1. Cadastrar como aluno
2. Cadastrar como admin
3. Voltar ao menu
      ''')
              escolha = input('Escolha uma opção: ')
              if escolha =='1':
                clear()
                print("\n===========CADASTRO DE ALUNO===========")  
                cadastrar (CadastroAluno,Aluno_conta)
                
          

              elif escolha == '2':
                clear()
                print("\n===========CADASTRO DE ADMIN===========")
                cadastrar (CadastroAdm,ADM_conta)
                


              elif opcao == '3':
                clear()
                return menu
              
              else:
                pass
                break
    



        elif opcao == '2':
          while True:

              print(f'''
{'========== LOGIN =========='}
1. Login como aluno
2. Login como admin
3. Voltar ao menu''')
              alternativa = input('Escolha uma opção: ')
              if alternativa =='1':
                clear()
                print("\n===========LOGIN DE ALUNO===========")  
                logar(LoginAluno,Aluno_conta)
                

              elif alternativa == '2':
                clear()
                print("\n===========LOGIN DE ADMIN===========")
                logar(LoginAdm,ADM_conta)
                

              elif opcao == '3':
                clear()
                return menu()
                

              else:
                pass
                break
            
        else:
            print(f'{red}Opção inválida. Tente novamente.{fim}')


menu()



















'''
'

print('ADM BOSTA')
cadastrar(CadastroAdm,ADM_conta)
logar(LoginAdm,ADM_conta)




print('Aluno bosta')
cadastrar(CadastroAluno,Aluno_conta)
logar(LoginAluno,Aluno_conta)
'''