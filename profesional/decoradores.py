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