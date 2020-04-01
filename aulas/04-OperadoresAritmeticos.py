# Exemplos de alguns operadores aritmeticos

print(10 + 10)
print(10 - 5)
print(10 * 5)
# Parte inteira da divisao
print(9 // 2)
# Resto da divisao entre dois valore
print(9 % 2)
# Potencia
print(2 ** 2)

# Precedencia dos operadores
print(10 + 2 * 4)
print((10 + 2) * 4)

# Salvar resultado dentro da variavel
valor1 = int(input("Informe o valor 1: "))
valor2 = int(input("Informe o valor 2: "))

somaValores = valor1 + valor2
print(f"A soma dos valores eh: {somaValores}")

subtracaoValores = valor1 - valor2
print(f"A subtracao dos valores eh: {subtracaoValores}")

multiplicacaoValores = valor1 * valor2
print(f"A multiplicacao dos valores eh: {multiplicacaoValores}")

mediaValores = (valor1 + valor2) / 2
print(f"Media dos valores: {mediaValores}")