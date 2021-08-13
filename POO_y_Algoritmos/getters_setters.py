
class Millas:
   """"
   def __init__(self, distancia):
      self.distancia = distancia
   """
   def convertir_a_kilometros(self):
      return (self.distancia * 1.609344)
   
   """
   ###### Con Getter y Setter Normal #######
   #Metodo getter
   def obtener_distancia(self):
      return self._distancia
   
   #metodo setter
   def definir_distancia(self, valor):
      if valor < 0:
         raise ValueError("No es posible convertir distancias menores a 0")
      self._distancia = valor
   """
   ########## Sin Getter y setter #######
   # Función para obtener el valor de _distancia
   
   """
   def obtener_distancia(self):
      print("Llamando al metodo getter")
      return self._distancia
   
   #Función para definir el valor de _distancia
   def definir_distancia(self, recorrido):
      print("Llamando al metodo setter")
      self._distancia = recorrido
   
   #funcion para eliminar el atributo _distancia
   def eliminar_distancia(self):
      del self._distancia
   
   distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)
   """
   ###   utilidad de decorador @property ###
   def __init__(self):
      self.distancia = 0
   
   # Función para obtener el valor de _distancia
   # Usando el decorador property
   @property
   def obtener_distancia(self):
      print("Llamar el metodo getter")
      return self._distancia
   
   # Función para definir el valor de _distancia
   @obtener_distancia.setter
   def definir_distancia(self, valor):
      if valor < 0:
         raise ValueError("No es posible convertir distancias menores a 0")
      print("Llamada al metodo setter")
      self._distancia = valor

#creamos un nuevo objeto
avion = Millas()

#indicamos la distancia
avion.definir_distancia=200

#obtenemos su atributo distancia
print(avion.definir_distancia)
