# deve importar a lib
from random import randrange, seed
import matplotlib.pyplot as plt

# print(randrange(0, 11))

seed(11)
notas_matematica = []

for notas in range(8):
    notas_matematica.append(randrange(0, 11))

print(len(notas_matematica))

x = list(range(1, 9))
y = notas_matematica

print(x[0:])
print(y[0:])

plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()