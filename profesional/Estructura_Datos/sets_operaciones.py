#union
my_set1 = {3,4,5}
my_set2 = {5,6,7}
my_set3 = my_set1 | my_set2 #uniendo los sets
print(my_set3)

#interseccion  ---  se queda solo con elementos en comun  
my_set4 = my_set1 & my_set2
print(my_set4)

#diferencia  -- quita los elementos del otro set y los que son iguales
my_set5 = my_set1-my_set2
print(my_set5)

my_set6 = my_set2-my_set1
print(my_set6)

#diferencia simetrica --- quita los elementos iguales, quedan los distintos
my_set6 = my_set1 ^ my_set2
print(my_set6)
