idades = [12, 32, 15, 28]
permissoes = []

def verifica_idades(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)

verifica_idades(idades, permissoes)
print(permissoes)

for permissao in permissoes:
    if permissao == True:
        print('Pode dirigir!')
    else:
        print('Não pode dirigir.')
