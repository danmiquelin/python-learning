class Animal:
    def emitir_som(self):
        print("Qualquer som ....")
        
class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau Miau!")  

Cachorro = Cachorro()
Cachorro.emitir_som()   

Gato = Gato()
Gato.emitir_som()   
      