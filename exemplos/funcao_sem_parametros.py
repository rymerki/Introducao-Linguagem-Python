# Funções sem parametros

def saudacao():
    nome = input('Qual o seu nome? ')
    print(f'Ola, {nome}!')

saudacao()

# funcao sem parametros
def verificar_idade():
    idade = input('Informe a sua idade: ')
    idade = int(idade)
    if idade >= 18:
        print('Você pode dirigir!')
    else:
        print('Você ainda nao pode dirigir.')

verificar_idade()