# Os operadores logicos sao responsaveis por testar se uma determinada comparacao entre dois ou mais valores sao verdadeiros.

idade = 61
if (idade <= 10):
    print("O paciente tem prioridade")
else:
    print("O paciente deve aguardar atendimento")

# Adicionando mais uma condicao
if (idade <= 10):
    print("O paciente tem prioridade")
elif (idade >= 60):
    print("O paciente tem prioridade nível 2")
else:
    print("O paciente deve aguardar atendimento")

# Tambem eh possivel definir o valor de uma variavel a depender do resultado de uma condicao logica, como podemos ver abaixo
prioridade = "Prioridade 1" if (idade <= 10) else "Prioridade 2"
print(prioridade)