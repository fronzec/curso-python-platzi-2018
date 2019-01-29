import copy

countries = ['México', 'Venezuela', 'Colombia', 'Argentina']
ages = [12, 18, 24, 34, 50]
weights = [12, 18, 24, 34, 50]
print(id(countries))
print(id(ages))
print(id(weights))

receta = ['Ensalada', 2, 'lechugas', 5, 'jitomates']
countries[0] = 'Ecuador'

name = 'David'
print(name[0])
# name[0] = 'd'  # Error Los strings son inmutables

# alias, apuntan al mismo objeto
global_countries = countries
print(id(countries))
print(id(global_countries))

countries[0] = 'Guatemala'
print(countries)
print(global_countries)

# Como copiar una lista en otra lista como objeto nuevo, usamos la lib copy
print('#' * 25)
global_countries = None
global_countries = copy.copy(countries)
# global_countries = countries[::] # Otra forma de crear una copia de una lista
print(id(countries))
print(id(global_countries))

countries[0] = 'Honduras'
print(countries)
print(global_countries)

# Ciclar sobre una lista
for country in countries:
    print(country)
