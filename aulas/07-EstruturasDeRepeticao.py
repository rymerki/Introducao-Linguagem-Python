# Objetivo entender o funcionamento do laco while, for e break

# While
numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número maior que 19 para encerrar o laço: "))
    soma = soma + numero
else:
    print("loop encerrado")
print(soma)

# For
for x in range(1, 10):
    y = x + 1
    print(y)
else:
    print("loop encerrado")
print(y)

# O comando break vai encerrar imediatamente o laço, assim que for chamado
numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número maior que 19 para encerrar o laço: "))
    soma = soma + numero
    if numero == 16:
       break
print(soma)

# o comando continue ignora a execução de um passo do loop quando uma determinada condição é satisfeita
numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número maior que 19 para encerrar o laço: "))
    soma = soma + numero
    if numero == 16:
       continue
print(soma)