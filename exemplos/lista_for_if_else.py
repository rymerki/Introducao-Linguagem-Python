# Listas

idades = [10, 11, 15, 18, 30, 50]

print(type(idades))
print(idades[3])
print(idades[0:])
print(idades[-1])
print(idades[:4])

# for fora da função
def verifica_idade(idade):
    if idade >= 18:
        print(f'{idade} anos de idade, TEM permissão para dirigir!')
    else:
        print(f'{idade} anos de idade, NÃO TEM permissão para dirigir!')

for idade in idades:
    verifica_idade(idade)

# for dentro da função
def verifica_idade_com_for(idades):
    for idade in idades:
        if idade >= 18:
            print(f'{idade} anos, PODE digirir!')
        else:
            print(f'{idade} anos, NÃO PODE dirigir')

verifica_idade_com_for(idades)