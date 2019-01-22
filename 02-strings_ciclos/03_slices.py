fruit = "banana"
fruit_slice = fruit[::2]
print('fruit[::2] = ', fruit_slice)

fruit_slice = fruit[3:3]
print('fruit[3:3] = ', fruit_slice)

fruit_slice = fruit[:]
print('fruit[:] = ', fruit_slice)

fruit_slice = fruit[1:-1:2]
print('fruit[1:-1:2] = ', fruit_slice)

print("*" * 12 + "Ejercicios interesantes" + "*" * 12)

print('Palindromos: Palabras que se leen igual de derecha a izquierda y viceversa')
var_string = 'Anita lava la tina'
print('var_string = ', var_string)
slice_string = var_string[::-1]
print("var_string[::-1]", slice_string)

var_string = 'Reconocer'
print('var_string = ', var_string)
slice_string = var_string[::-1]
print("var_string[::-1]", slice_string)

var_string = 'NO DI MI DECORO, CEDÍ MI DON'
print('var_string = ', var_string)
slice_string = var_string[::-1]
print("var_string[::-1]", slice_string)

print('Chascarillo del chavo del 8')

var_string = 'Lamina elizabet'
print('var_string = ', var_string)
slice_string = var_string[::-1]
print("var_string[::-1]", slice_string)

print("*" * 12 + "Jugando con frases" + "*" * 12)
print('\n')

var_string = '¡Has hoy lo que debas'
print('var_string = ', var_string)
slice_string = var_string[:5]
print("slice_string = var_string[:5] = ", slice_string)
print('\n')

var_string = 'y te sentiras tan bien'
print('var_string = ', var_string)
slice_string += var_string[:2]
print("slice_string = var_string[:2] = ", slice_string)
print('\n')

var_string = 'que mañana harás lo que se te de la gana,'
print('var_string = ', var_string)
slice_string += var_string[36:40]
print("slice_string = var_string[36:40] = ", slice_string)
print('\n')

var_string = 'Así que propontelo y lo lograrás!'
print('var_string = ', var_string)
slice_string += var_string[29:]
print("slice_string = var_string[29:] = ", slice_string)
print('\n')

print('slice_string = ', slice_string)

input()
