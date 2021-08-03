def divisors(num):
   divisors = []
   for i in range(1, num+1):
      if num % i == 0:
         divisors.append(i)
   return divisors

def run():
   num = input("Ingresar un numero : ")
   #estructura de excepciones con assert 
   #assert condicion, mensaje de error
   assert num.isnumeric() and int(num) > 0, "Debes ingresar un numero positivo"
   print(divisors(int(num)))
   print("programa termino")

if __name__ == "__main__":
   run()
