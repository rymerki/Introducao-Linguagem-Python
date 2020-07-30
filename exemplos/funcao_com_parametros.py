# Função com parametros

nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
idade = int(idade)

def verificar_idade_parametro(nome, idade):
    if idade >= 18:
        print(f'{nome}, você pode dirigir!')
    else:
        print(f'{nome}, você ainda não pode dirigir, pois tem apenas {idade} anos.')

verificar_idade_parametro(nome, idade)