objetivo = int(input('Escoge un numero : '))
epsilon = 0.01 # margen de error
paso = epsilon**2 # valor que se sumara secuencialmente hasta encontrar una raiz cuadrada
respuesta = 0.0

#mientras que respuesta al  cuadrado no sea igual al objetivo(con un margen de error de 0.01
# es decir epsilon), este while se seguira ejecutando
#respuesta <= objetivo: codigo defensivo; si respuesta es mayor a objetivo, el while sguira
#inifinitamente , nunca encontrara a la raiz cuadrada
#la raiz cuadrada nunca sera mas grande que el objetivo 
while abs(respuesta**2 - objetivo)>= epsilon and respuesta <= objetivo:
   print(abs(respuesta**2-objetivo), respuesta)
   respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
   print(f'No se encontro la raiz cuadrada {objetivo}')
else:
   print(f'la raiz cuadrada de {objetivo} es {respuesta}')