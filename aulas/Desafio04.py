# Fatorial
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for x in range(1, n + 1):
    fatorial = fatorial * x
print(fatorial)

# Imprimir a tabuada
num = int(input('Digite um número para ver sua tabuada: '))

for cont in range(1, 11):
    print('{} x {:2} = {}'.format(num, cont, num*cont))

