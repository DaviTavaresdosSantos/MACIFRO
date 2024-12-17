'''Turma: Informática 2A
Integrantes:  Davi Tavares dos Santos, WILLIAM CAVALCANTE DAMACENO, Júlia Marcelly Braga Belchior, João Vitor Silva Maciel, Layra Vitória Mota Leal'''

from login import LoginAdm,LoginAluno
from cadastro import CadastroAdm, CadastroAluno
from carrinho import Carrinho
from extra import red,fim, clear,green
from comida import Lanche,Almoco
from bebida import Bebida
from random import randint,choice
import string



'Informações'
salgadoAssado = Lanche(6.0,'Salgado Asssado','Temos de carne e preseunto e queijo,',1)
salgadoFrito = Lanche(5.0,'Salgado Frito','Temos de carne e preseunto e queijo,',1)
Pao_de_queijo = Lanche(6.0,'Pão de quijo','Temos apenas sabor queijo',1)
refeicao = Almoco(5.0,'Almoco','coisa ai ',1,0)
refrigerante = Bebida ("refrigerante", 'refrigerante de cola', 5.0 , 1 , 350)
agua = Bebida ("agua", 'agua', 2.0 , 1 , 250)
suco = Bebida ("suco", "uva" , 4.0 , 1 , 450)

aluno = CadastroAluno('davi','1234','usdfsfdsf')
ADM = CadastroAdm('davi','1234','fdsfdf','101')
'------------------------------------------------------------------------------------'


'Contas'
ADM_conta = [ADM]
Aluno_conta = [aluno] # Exemplo de conta
'---------------------------------------------------'




def cadastrar(subclasse,lista: list):

  nome = input('Digite seu nome:')
  senha = input('Digite seu senha:')
  email = input('Digite seu email:')
  objeto_acessor = subclasse(nome, senha, email)
  objeto_acessor.Cadastro(lista,objeto_acessor)
  
def logar(subclasse,lista: list):  

  global objeto_acessor
  nome = input('Informe seu nome:')
  senha = input('Informe sua senha:')
  
  objeto_acessor = subclasse(nome, senha,False)
  objeto_acessor.verificar(lista)


  


def Interface_Aluno():   #A classe "comprar" virou uma função
    Usuario_Carrinho = Carrinho()
    
    while True: 
        try:
            Interface = input('''Informe uma opção: 
        1. Comida
        2. Bebida
        3. Carrinho
        4. Remover
        5. Finalizar
        6. Sair
        R:''')
            
            if Interface == '1':
                clear
                Interface_comida = input(''' De comida Temos: 
    1.Salgado frito
    2.salgado assado
    3.Pão de queijo
    4.Almoço
    R: ''')
                if Interface_comida == '1':
                    quantidadeAtual = int(input('Informe a quantidade:'))
                    salgadoFrito.qtd = quantidadeAtual
                    salgadoFrito.atualizar()
                    Usuario_Carrinho.AdicionarItens(salgadoFrito)
                

                elif Interface_comida == '2':
                    quantidadeAtual = int(input('Informe a quantidade:'))
                    salgadoAssado.qtd = quantidadeAtual
                    salgadoAssado.atualizar()
                    Usuario_Carrinho.AdicionarItens(salgadoAssado)

                elif Interface_comida == '3':
                    quantidadeAtual = int(input('Informe a quantidade:'))
                    Pao_de_queijo.qtd = quantidadeAtual
                    Pao_de_queijo.atualizar()
                    Usuario_Carrinho.AdicionarItens(Pao_de_queijo) 

                elif Interface_comida == '4':
                    peso = int(input('Nós informe o peso da sua comida: '))
                    horario = float(input('Informe o horário: '))
                    refeicao.Peso = peso
                    refeicao.horario = horario
                    refeicao.atualizar()
                    Usuario_Carrinho.AdicionarItens(refeicao)
                
                
            elif Interface == '2':
                clear()
                Interface_bebida = input(''' De Bebida Temos: 
    1.Coca_cola
    2.Água
    3.Suco
    R: ''')
                
                if Interface_bebida == '1':
                    quantidadeAtual = int(input('Informe a quantidade:'))
                    refrigerante.qtd = quantidadeAtual
                    refrigerante.atualizar()
                    Usuario_Carrinho.AdicionarItens(refrigerante)

                elif Interface_bebida == '2':
                    quantidadeAtual = int(input('Informe a quantidade:'))
                    agua.qtd = quantidadeAtual
                    agua.atualizar()
                    Usuario_Carrinho.AdicionarItens(refrigerante)

                elif Interface_bebida == '3':
                    quantidadeAtual = int(input('Informe a quantidade:'))
                    suco.qtd = quantidadeAtual
                    suco.atualizar()
                    Usuario_Carrinho.AdicionarItens(suco)

                else:
                    print('Valor invalido')
                    pass

            elif Interface == '3':
                clear()
                Usuario_Carrinho.ExibirIntens()  

            elif Interface == '4':
                clear()
                Usuario_Carrinho.RemoverIntens()

            elif Interface == '5':
                clear()
                if len(Usuario_Carrinho.verificarTamanho())<= 0:
                    print('Carinho vazio, impossivel finalizar a compra!!')

                else:
                    clear()
                    
                    print(f'''{green}Compra realizada com sucesos. Retirar na cantina
    Levar o código abaixo: {fim}''')
                    
                    
                    for c in range(11):
                        letra = choice(string.ascii_lowercase)
                        numero = randint(1,100)
                        ordem = randint(1,10)
                        if ordem >=5:
                            print(letra, end = '')

                        else:
                            print(numero, end = '')  
                    menu()




            elif Interface == '6':
                break
        

        except ValueError:
            print(f'{red}Valor informado não corresponde ao solicitado{fim}')





#interfface do administrador
def Interface_ADM():
    while True: 
        clear()
        print('''========Seja bem vindo a página de administração========''')
    
        Interface = input('''O que deseja alterar:
1. Comida
2. Bebida
3. Sair
R: ''')

        if Interface == '1':
            clear()
            Interface_comida = input('''=================================
Digite qual comida deseja alterar o valor: 
1. Salgado frito
2. Salgado assado
3. Pão de queijo
4. Almoço
R: ''')

            if Interface_comida == '1':
                clear()
                while True:
                    try:
                        valor = float(input('''======================================
Valor atual do Salgado frito: 5
Informe o novo valor do Salgado frito: '''))
                        ADM.alterar_Valor(salgadoFrito, valor)
                        break
                    except ValueError:
                        print((f'{red}Erro: Por favor, insira um número válido.{fim}'))

            elif Interface_comida == '2':
                clear()
                while True:
                    try:
                        valor = float(input('''======================================
Valor atual do Salgado assado: 6
Informe o novo valor do Salgado assado: '''))
                        ADM.alterar_Valor(salgadoAssado, valor)
                        break
                    except ValueError:
                        print("Erro: Por favor, insira um número válido.")

            elif Interface_comida == '3':
                clear()
                while True:
                    try:
                        valor = float(input('''======================================
Valor atual do Pão de queijo: 6
Informe o novo valor do Pão de queijo: '''))
                        ADM.alterar_Valor(Pao_de_queijo, valor)
                        break
                    except ValueError:
                        print("Erro: Por favor, insira um número válido.")

            elif Interface_comida == '4':
                clear()
                while True:
                    try:
                        valor = float(input('''==================================
Valor atual do Almoço: 5
Informe o novo valor do Almoço: '''))
                        ADM.alterar_Valor(refeicao, valor)
                        break
                    except ValueError:
                        print("Erro: Por favor, insira um número válido.")


#interface das bebidas

        elif Interface == '2': 
            Interface_bebida = input('''Oque deseja alterar: 
1. Coca cola
2. Água
3. Suco
R: ''')

            if Interface_bebida == '1':
                while True:
                    try:
                        valor = float(input('''==================================
Valor atual da Coca cola: 
Informe o novo valor da Coca cola: '''))
                        ADM.alterar_Valor(refrigerante, valor)
                        break
                    except ValueError:
                        print("Erro: Por favor, insira um número válido.")

            elif Interface_bebida == '2':
                while True:
                    try:
                        valor = float(input('''==================================
Valor atual da Água: 
Informe o novo valor da Água: '''))
                        ADM.alterar_Valor(agua, valor)
                        break
                    except ValueError:
                        print("Erro: Por favor, insira um número válido.")

            elif Interface_bebida == '3':
                while True:
                    try:
                        valor = float(input('''==================================
Valor atual do Suco: 
Informe o novo valor do Suco: '''))
                        ADM.alterar_Valor(suco, valor)
                        break
                    except ValueError:
                        print("Erro: Por favor, insira um número válido.")

            else:
                print('Valor inválido')
                pass

        elif Interface == '3':
            break
        else:
            print('Valor inválido')


def menu():
    global objeto_acessor, ADM_conta, Aluno_conta, clear, finalizar

    while True:
        
        print(f'''
{'========== MENU =========='}
Olá, seja bem vindo ao MecIFRO, o que você deseja fazer?
1. Cadastrar 
2. Login
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
                if escolha == '1':
                    clear()
                    print("\n===========CADASTRO DE ALUNO===========")  
                    cadastrar(CadastroAluno, Aluno_conta)

                elif escolha == '2':
                    clear()
                    print("\n===========CADASTRO DE ADMIN===========")
                    cadastrar(CadastroAdm, ADM_conta)

                elif escolha == '3':
                    clear()
                    return menu()
                
                else:
                    break

        elif opcao == '2':
            clear()
            while True:
                print(f'''
{'========== LOGIN =========='}
1. Login como aluno
2. Login como admin
3. Voltar ao menu''')
                alternativa = input('Escolha uma opção: ')
                if alternativa == '1':
                    clear()
                    print("\n===========LOGIN DE ALUNO===========")  
                    logar(LoginAluno, Aluno_conta)
                    if objeto_acessor.status == True:
                        print(f'{green}Login realizado com sucesso{fim}')
                        Interface_Aluno()
                    else:
                        print(f'{red}Valores incorretos{fim}')
                    
                elif alternativa == '2':
                    clear()
                    print("\n===========LOGIN DE ADMIN===========")
                    logar(LoginAdm, ADM_conta)
                    if objeto_acessor.status == True:
                        print(f'{green} Login realizado com sucesso{fim}')
                        Interface_ADM()

                    else:
                        pass

                elif alternativa == '3':
                    clear()
                    return menu()
                
                else:
                    print(f'{red}Opção inválida. Tente novamente.{fim}')
            

menu()
