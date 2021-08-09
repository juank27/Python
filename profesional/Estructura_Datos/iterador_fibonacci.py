import time

class FiboIter():
   
   def __iter__(selft):
      selft.n1 = 0
      selft.n2 = 1
      selft.counter = 0
      return selft
   
   def __next__(selft):
      if selft.counter == 0:
         selft.counter += 1
         return selft.n1
      elif selft.counter == 1:
         selft.counter += 1
         return selft.n2
      else:
         selft.aux = selft.n1 + selft.n2
         #selft.n1 = selft.n2
         #selft.n2 = selft.aux
         selft.n1, selft.n2 = selft.n2, selft.aux
         selft.counter += 1
         return selft.aux

if __name__ == "__main__":
   fibonacci = FiboIter()
   for element in fibonacci:
      print(element)
      time.sleep(0.05)