# Uma classe é a representação de um elemento do mundo real a ser reproduzido em um software.
# uma classe pode ser considerada como um molde de objetos.
# def __init__(self) é usado para inicializar o objeto quando vai criar uma instancia de uma classe (metodo construtor)
# self é um parametro obrigatorio que recebera a instancia criada

class Usuario:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade