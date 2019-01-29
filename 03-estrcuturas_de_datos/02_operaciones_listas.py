import random

my_list_a = list(range(0, 10))
my_list_b = list(range(10, 20))

print(my_list_a)
print(my_list_b)
# Operaciones
print('#' * 30)
print(my_list_a + my_list_b)
print(my_list_a * 2)

# append
print('#' * 30)
my_list_a.append(10)
print(my_list_a)

# pop
print('#' * 30)
print(my_list_a.pop())
# print(my_list_a.pop(0))#Using an index
print(my_list_a)

# del
print('#' * 30)
my_list_a.append(99)
print(my_list_a)
del my_list_a[-1]  # deleting last index
print(my_list_a)

# sorting the list
print('#' * 30)
my_list_a.sort(reverse=True)
print(my_list_a)

# Sort

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0, 15))
print(random_numbers)

# Usando la funcion sorted para ordenar una lista, en este caso no se modifica la lista original
ordered_numbers = sorted(random_numbers)
print(ordered_numbers)

# Si usamos la funcion sort de la lista la lista si es modificada
random_numbers.sort()
print(random_numbers)
