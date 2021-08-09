import time

class FiboIter():
   
   def __init__(selft, max = None):
      if max == None:
         selft.max = None
      else:
         selft.max = max
   
   def __iter__(selft):
      selft.n1 = 0
      selft.n2 = 1
      selft.counter = 0
      return selft
   
   def __next__(selft):
      def fibo(): #funcion fibonacci
         selft.aux = selft.n1 + selft.n2
         #selft.n1 = selft.n2
         #selft.n2 = selft.aux
         selft.n1, selft.n2 = selft.n2, selft.aux
         selft.counter += 1
         return selft.aux
      
      if selft.counter == 0:
         selft.counter += 1
         return selft.n1
      elif selft.counter == 1:
         selft.counter += 1
         return selft.n2
      elif selft.max == None:
         return fibo() #ejecucion infinita
      elif selft.counter >= selft.max:
         raise StopIteration
      else:
         return fibo()#ejecucion controlada

if __name__ == "__main__":
   fibonacci = FiboIter()
   i  = 0
   for element in fibonacci:
      print(str(i) + " Vueltas")
      print(element)
      time.sleep(0.05)
      i += 1