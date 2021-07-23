#tipos de datos sencillos
#String
nombre = "Juan"
nombre2 = "Carlos"
#concatenar cadenas 
nombre_completo = nombre + nombre2

#char
caracter = 'c'

#int
n = 5

#float
n1 = 5.0

#boolean
estado = True
estado2 =False
#input - ingreso de datos por terminal
numero1 = input("Escribir un numero: ")
numero1 = int(numero1) #convertir a entero
texto = str(numero1) #pasar de int a text

#operadores logicos y de compracion
es_estudiante = True
trabaja = False
#operador and para que sea true las dos se deben cumplir
accion = es_estudiante and trabaja
#operador or para que sea falso las dos son falsas
accion = es_estudiante or trabaja
#not negacion, cambia su estado
accion = not trabaja
# igualdad == verofica que los dos sean igual return True
number1 = 5
number2 = 5
number1 == number2
# diferente != retorna true si los dos son distintos
number1 != number2
#operador > < >= <=