# Simulador de dados
# Simular o uso de um dado , gerando um valor de 1 ate 6

import random


class SeimuladordeDado:
    def _init_(self):
        self.min = 1
        self.max = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado"

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == "sim":
            self.GerarValordoDado()

    def GerarvalordoDado(self):
        print(random.randint(self.min, self.max))