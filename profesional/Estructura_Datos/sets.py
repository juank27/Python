#ejemplo de sets, elementos inmutables he irrepetibles
#crear un set vacio
my_set_principal = set()

my_sett = {3,4,5}
print("mi_set = ", my_sett)

my_set2 = {"hola", 23.3, False, True}
print("mi_set2 = ", my_set2)

#borra los elementos repetidos
my_set4 = {3,3,2}
print("mi_set4 = ", my_set4)

#error de un set , la lista se puede modificar
#my_set3 = {[1,2,3], 4}
#print("mi_set3 = ", my_set3)

#convertir a set
my_list = [1,1,2,3,4,4,5]
my_set_List = set(my_list)
print(list)

my_set = {1, 2, 3}

# Añadir un elemento
my_set.add(4)

# Añadir varios elementos
my_set.update([1, 2, 5])
my_set.update((1, 7, 2), {6, 8})

# Borrar un elemento existente
my_set.discard(1)
my_set.remove(2)

# Borrar un elemento inexistente
my_set.discard(10)  # No hay problema
my_set.remove(10)  # Error, ese elemento no existe

# borrar elemento aleatorio
my_set.pop()

# Borrar todos los elementos
my_set.clear()  