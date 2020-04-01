# Objetivo: armazenar dados digitados no teclado em variaveis

# Como?
# Atraves do metodo input
# Por padrao o metodo input salva todas as variaveis no formato str, se quiser salvar em outro formato eh necessario converter

nome = input("Digite o seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
# convertendo a variavel idade para o formato int
idade = int(input("Digite a sua idade: "))

print(type(idade))
print(f"Olá {nome} {sobrenome}, sua idade é {idade}.")