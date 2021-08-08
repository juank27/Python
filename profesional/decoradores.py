#ejemplo de decorador
def  decorador(func):
   def envoltura():
      print('esto se añade a mi funcion original')
      func()
   return envoltura

def saludo():
   print("Hola!!")

saludo()
# Output
# Hola!!

saludo = decorador(saludo)
saludo()
# Output
# Esto se añade a mi funcion original 
# Hola!!

########## ejemplo de decoradores #########
def mayusculas(func):
   def envoltura(texto):
      return func(texto).upper()
   return envoltura

@mayusculas #forma directa de decirle que es un decorador
def mensaje(nombre):
   return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))