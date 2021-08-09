def my_gen ():
   """ Ejemplo de generadores """
   print("Hello world")
   n = 0
   yield n
   
   print('Hello heaven!')
   n = 1
   yield n
   
   print('Hello hell')
   n = 2
   yield n
   
a = my_gen()
print(next(a)) #Hello world
print(next(a)) #Hello heaven!
print(next(a)) #Hello hell
#print(next(a)) # StopIteration

my_list = [1,2,3,4,5,6,7,8,9]
my_second_list = [x*2 for x in my_list] #List comprehension
my_second_gen = (x*2 for x in my_list) # Generator expression
b = my_second_gen

while True:
   try:
      element = next(b)
      print(element)
   except StopIteration:
      break
