## Estructuras de datos
# Listas
Las listas son secuencias de valores

Ej:
```
[2,5,6]
['México','Colombia']
```
Las listas son mutables a diferencia de los strings

```
my_lits = [1,2,3]
my_lits[2] = 6
```

Los indices de las listas funcionan igual que los strings
A diferencia de los strings cada lista vive en un lugar diferente de la memoria
Las listas se inician con [] o con la funcion list
Para crer una copia de una lista podemos usar la lib copy `the_copy = copy.copy(the_var)`

## Operaciones en listas
El operador +(suma) concatena dos o más listas.
El operador *(multiplicación) repite los elementos de la misma lista tantas veces los queramos multiplicar.
Las listas tienen varios metodos que podemos utilizar.
- `append` nos permite añadir elementos a listas. Cambia el tamaño de la lista.
- `pop` nos permite sacar el último elemento de la lista. También recibe un índice y esto nos permite elegir qué elemento queremos eliminar.
- `sort` modifica la propia lista y ordenarla de mayor a menor. Existe otro método llamado `sorted`, que también ordena la lista, pero genera una nueva instancia de la lista
- `del` nos permite eliminar elementos vía indices, funciona con slices
- `remove` nos permite es pasarle un valor para que Python compare internamente los valores y determina cuál de ellos hace match o son iguales para eliminarlos.