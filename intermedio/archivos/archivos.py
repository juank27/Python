#lectura de archivos
def read():
   numbers = []
   with open("./intermedio/archivos/archivos.txt", "r", encoding="utf-8") as f :
      for line in f:
         numbers.append(int(line))
   print(numbers)
#Escritura de archivos
def write():
   names = ["Facundo", "Miguel","Pepe", "Juan", "Rocío"]
   with open("./intermedio/archivos/names.txt", "w", encoding="utf-8") as f:
      for name in names:
         f.write(name)
         f.write("\n")
#Ejecucion
def run():
   #read()
   write()

if __name__ == '__main__':
   run()