## ¿Que es la programación?
- Un programa es una secuencia de instrucciones que describe como realizar un cómputo
- Casi todos los programas realizan las siguientes tareas:
    - input
    - output
    - Operaciones matematicas
    - Ejecucion condicional
    - Repeticiones
- Objetivos del curso
    - Aprender a pensar como un Cientifico de computo
    - Aprender a usar python
    - Entender las ventajas y desventajas de python
    - Aprender a construir una aplicacion de linea de comandos
- ¿Por qué programar con python?
    - Tiene una amplia comunidad
    - Facil para principantes
    - Popularidad, top 5 lenguajes segun Github
    - Tiene un conjunto de Librerias más amplito pypi.
    - Varios de los gigantes y startups de la industria lo usan, dar mucha velocidad al programador.
    - "Python cuando podamos, C++ cuando necesitemos" - Google.
- Algunos comandos importantes
- `python --version` para obtener la version de pyt

### Operadores
Python tiene los siguientes tipos de operadores:
- Operadores aritmeticos: +,-,*,//,…
- Operadores de comparación(Relacionales) : ==, !=,<, >,…
- Operadores de asignación: =, +=, -= //=, …
- Operadores logicos: and, or, not
- Operadores binarios: &, |, ^, ~, <<, >>
- Membership Operators: in, not in
- Operadores de identidad: is, not is
- Un punto importante a la hora de programar es conocer la precedencia de los operadores
- [Más info aqui](https://www.geeksforgeeks.org/basic-operators-python/)

- Los operadores son contextuales, dependen del tipo de valor.
- Para obtener el tipo de un valor usamos la funcion `type(<valor>)`
- Es importante conocer el tipo de un valor ya que dependiendo del tipo los operadores van a funcionar de manera diferente
- Hay operadores que no funcionan en ciertos tipos de datos

### Variables y expresiones
Una **variable** es simplemente el contenedor de un valor. Es una forma de decirle a la computadora de que nos guarde un valor para luego usarlo.

Python es un lenguaje dinámico, este concepto de privado y público se genera por convenciones del lenguaje. En programación el signo `=` significa asignación.

Si una variable esta en mayúscula, usualmente se refiere a una constante, no debería reasignarse. Es una convención.

**Reglas de variables**
- Pueden contener números y letras
- No deben comenzar con número
- Múltiples palabras se unen con `_`
- No se pueden utilizar palabras reservadas: `False`, `for`, `class`, `or`, etc.

**Convenciones de python**

En python no existen como tal los modificadores de acceso, más bien es por convención,
- Las variables 'privadas' empiezan con `_`, no deben ser modificadas.
- Los nombres de las 'constantes' estan en mayuscula por ejempl:`PI`, no deben ser modificadas.
- Las variables que empiezan con doble guion bajo signican 'No toques esto por qu se rompe', por ejemplo: `__esto_es_importante` (Variables superprivadas)

**Expresiones**: son instrucciones para el interprete para evaluar la expresión. Los enunciados(statements) tienen efectos dentro del programa, como `print()` que genera un output.

Para evaluar una expresion python usa la precedencia de operadores.

**PEMDAS** = Paréntesis, Exponente, Multiplicación, Adicción, Substracción

### Paquetes de terceros PyPi(Python package index)
PyPi es un repositorio de librerias para python.

La forma de instalar paquetes en nuestro sistema es a travez de `pip`

Es buena practica mantener varios entornos para cada aplicación, esto lo podemos hacer usando el paquete `virtualenv`,
el cual nos permite tener entornos aislados con dependencias diferentes para cada aplicación.


### Funciones
En el contexto de la programación las funciones son simplemente una agrupación de enunciados(statments) que tienen un nombre. Una función tiene un nombre, debe ser descriptivo, puede tener parámetros y puede regresar un valor después que se generó el cómputo.

Python es un lenguaje que se conoce como *batteries include*(baterías incluidas) esto significa que tiene una librería estándar con muchas funciones y librerías.

Para declarar funciones que no son las globales, las *built-in functions*, necesitamos importar un módulo [Ver más](https://docs.python.org/3/library/functions.html).

Con el keyword `def` declaramos una función.

Para usar funciones que se encuentran en otros modulos necesitamos importar esos modulos

Las funcones se pueden componer, es decir una funcion puede ponerse como parametro de otra, esto lo que hara sera evaluar la primera y regresar el resultado le cual sera usado por la funcion externa.

Los argumentos de las funciones pueden ser posicionales(positional arguments) o con nombre (named arguments)

El orden de ejecución es de arriba hacia abajo y de izquierda a derecha