# Uma lista é uma estrutura de dados representada como uma sequencia de objetos separados por vírgula,
# podendo armazenar qualquer tipo de dado e ser alterada a qualquer momento.

# Para declarar uma lista no Python, utilizamos
# nome_da_lista = [elemento1, elemento2, elemento3]

# Para inserir novos elementos em uma lista, utilizamos o metodo append().
# Este metodo ira inserir determinado elemento ao final da lista em questao:

lista = ["Arroz", "Feijao"]
lista.append("Macarrão")
print(lista)

# Para inserir elementos em uma determinada posicao de uma lista, utilizamos o metodo insert().
# Este metodo recebe como parametro o elemento a ser inserido e sua posicao
lista2 = ["Arroz", "Feijão"]
lista2.insert(1, "Goiabada")
print(lista2)

# Para remover elementos de uma lista, utilizamos o metodo remove().
# Este metodo recebe como parametro o elemento a ser removido.
lista3 = ["Chocolate", "Pizza"]
lista3.insert(1, "Refrigerante")
print(lista3)
lista3.remove("Chocolate")
print(lista3)

# Outros meios para manipular listas
# pop(índice): remove o elemento da lista;
# index(elemento): retorna o índice do elemento na lista;
# count(elemento): retorna a quantidade de vezes em que um elemento aparece na lista;
# sort(): ordena a lista;
# reverse(): inverte a ordem da lista.

lista3.pop(1)
print(lista3)

print(lista2.index("Goiabada"))