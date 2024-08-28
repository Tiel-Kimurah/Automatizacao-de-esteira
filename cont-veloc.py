


#importacao da biblioteca de tempo
import time 

#inicio 
class EsteiraIndustrial:
    def __init__(self):
        self.velocidade = 0 #velocidade inicial da esteira
    def definir_velocidade(self, nova_velocidade):
        if nova_velocidade < 0:
            print("A velocidade nao pode ser negativa. definindo para 0")
            nova_velocidade = 0
        elif nova_velocidade > 100:
            print("velocidade maxima e 100. ajustando para 100")
            nova_velocidade = 100
        self.velocidade = nova_velocidade
        print(f"velocidade ajustada para {self.velocidade}.")
    def iniciar(self):
        print("esteira  iniciada")
        while True:
            #simulacao de comportamento da esteira
            print(f"velocidade atual: {self.velocidade}")
            time.sleep(1) # a cada segundo, exibe a velocidade
    def parar(self):
        print("esteira parada")
        self.velocidade = 0

#exemplo de uso
if __name__ == "__main__":
    esteira = EsteiraIndustrial()
    #ajuste de velocidade
    velocidade_desejada = int(input("digite a velocidade desejada (0-100):"))
    esteira.definir_velocidade(velocidade_desejada)

    try:
        #inicia a esteira
        esteira.iniciar()
    except KeyboardInterrupt:
        #permite parar a esteira com ctrl+c
        esteira.parar()