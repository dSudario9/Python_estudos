

import random

class Simuladordedados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = " Você gostaria de gerar um novo valor para o dado ?"

    def Iniciar(self):
        resposta =input(self.mensagem)
        try:
            if resposta == "sim" or resposta == "s":
                self.gerarvalordodado()
            elif resposta == "nao" or resposta == "n":
             print ("Agradecemos a sua participação")
        except:
            print("Ocorreu um erro ao receber sua resposta")

    def gerarvalordodado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = Simuladordedados()

simulador.Iniciar()


