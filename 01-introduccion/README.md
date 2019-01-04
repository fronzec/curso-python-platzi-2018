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