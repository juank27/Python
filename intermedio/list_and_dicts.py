def run():
   my_list = [1,"hello", True, 4.5]
   my_dict = {"firstname": "Juan Carlos", "lastname": "Ruiz"}
   super_list = [
      {"firstname": "Juan Carlos", "lastname": "Ruiz"},
      {"firstname": "Juan ", "lastname": "Rosendo"},
      {"firstname": "Andres", "lastname": "Carreño"},
      {"firstname": "Elena", "lastname": "Gomez"},
      {"firstname": "Carlos", "lastname": "Montaño"}
   ]
   for i in super_list:
      print(i)
   super_dict = {
      "natural_nums" : [1,2,3,4,5],
      "integer_nums" : [-1,-2,0,1,2],
      "floating_nums" : [1.1,4.5,6.43]
   }
   #imprimir el super_dict
   for key, value in super_dict.items():
      print(key, "-", value)

#inicia con la funcion main
if __name__ == '__main__':
   run()