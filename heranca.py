## PARA NAO DAR AZAR!!!!
print('Hello World!')

##INICIO

class Carro:
    numero_rodas = 4  # Atributo de classe
    quantidade_passageiros = 5  # Atributo de classe

    def acelerar (self):
        print("Acelerando...")
        
    def frear (self):
        print("Freando...")
        
    def buzinar (self):
        print("Buzinando...")   
        
class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 1992
   
  
uno = Uno() 
uno.acelerar()  # Acessando método da classe pai
print(uno.numero_rodas)  # Acessando atributo de classe

