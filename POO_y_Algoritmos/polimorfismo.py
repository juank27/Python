
class Persona:
   
   def __init__(self, nombre) :
      self.nombre = nombre
   
   def avanza(self):
      print("Voy caminando")

class Ciclista(Persona):
   
   def __init__(self, nombre):
      super().__init__(nombre)
   
   def avanza(self): #reescribe avanza de la clase padre, persona
      print('Voy moviendome en Bicicleta')

def main():
   persona = Persona('David')
   persona.avanza()
   
   ciclista = Ciclista('Daniel')
   ciclista.avanza()

if __name__ == '__main__':
   main()