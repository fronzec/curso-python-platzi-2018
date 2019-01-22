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
palindromo = 'Anita lava la tina'
print('var_string = ', palindromo)
slice_string = palindromo[::-1]
print("var_string[::-1]", slice_string)

palindromo = 'Reconocer'
print('var_string = ', palindromo)
slice_string = palindromo[::-1]
print("var_string[::-1]", slice_string)

input()
