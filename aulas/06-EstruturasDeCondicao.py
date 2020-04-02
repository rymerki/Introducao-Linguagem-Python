# Objetivo: entender melhor o funcionamento das estreturas if e else

nome, idade, sobrenome = "João", 20, "Silva"
print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

nome2 = input("Digite seu nome: ")
sobrenome2 = input("Digite seu sobrenome: ")
idade2 = int(input("Digite sua idade: "))
print(f"Olá, {nome2} {sobrenome2}, sua idade é: {idade2}")

mediaIdades = (idade + idade2) / 2
print(f"A média das idades é: {mediaIdades}")

if (idade >= 18):
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} não é maior de idade.")

if (idade2 <= 17):
    print(f"{nome2} é adolescente.")
elif (idade2 >= 18 and idade2 <= 50):
    print(f"{nome2} é adulto.")
else:
    print(f"{nome2} é idoso.")
