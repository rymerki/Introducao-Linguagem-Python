# Objetivo: entender o que sao atribuidores de atribuicao
# Atribuicao eh a forma em que se define um valor referente a determinada variavel

# Exemplo

x = 10
y = "Teste"
print(type(x))
print(type(y))

nome, idade, sobrenome = "João", 20, "Silva"

print(nome, sobrenome, idade)
print("Ola")

# Concatenando frase com variaveis de duas maneiras
print("Ola, meu nome é", nome, sobrenome,"tenho", idade, "anos.")
print(f"Olá, meu nome é {nome} {sobrenome}, tenho {idade} anos.")

altura = 1.70
print(altura)
