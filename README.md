# Autómata de Pila

Este proyecto simula un autómata de pila (AP), un tipo de autómata que es más poderoso que los autómatas finitos y es capaz de reconocer lenguajes libres de contexto. En específico, el autómata de pila implementado aquí es capaz de reconocer un subconjunto de lenguajes libres de contexto según la definición y las reglas de transición dadas.

## Descripción

El autómata de pila implementado está definido por la siguiente tupla:

```
P = {Q, Σ, Γ, q0, Z0, δ, F },
```

donde:

- `Q`: Conjunto de estados `{q0, q1, q2}`
- `Σ`: Alfabeto de entrada `{0, 1}`
- `Γ`: Alfabeto de la pila `{X, Z0}`
- `q0`: Estado inicial
- `Z0`: Símbolo inicial de la pila
- `δ`: Funciones de transición
- `F`: Conjunto de estados de aceptación `{q2}`

Las funciones de transición `δ` son las siguientes:

- `δ(q0, 0, Z0) = (q0, XXZ0)`
- `δ(q0, 0, X) = (q0, XX)`
- `δ(q0, 1, X) = (q1, ε)`
- `δ(q1, 1, X) = (q1, ε)`
- `δ(q1, ε, Z0) = (q2, Z0)`

## Características

- Simula un autómata de pila basado en una estructura de pila.
- Puede procesar cadenas de entrada compuestas de `0`s y `1`s y determinar si son aceptadas o no.
- Incluye la capacidad de reiniciar el estado del autómata para procesar una nueva cadena de entrada.

## Cómo usar

Para ejecutar el autómata de pila, necesita tener Python instalado en su máquina. Clone o descargue este proyecto y ejecute el script `automata_de_pila.py`.

```bash
python automata_de_pila.py
```

Dentro del script, puede modificar el array `cadenas` para probar diferentes cadenas de entrada y observar si son aceptadas por el autómata.

```python
cadenas = ["00", "0001", "01", "001", "00011", "11"]
```

El script imprimirá en la consola si cada cadena es aceptada o no por el autómata.

## Ejemplos

Al ejecutar el script, verá resultados en la consola similares a estos:

```
La cadena '00' es aceptada por el autómata.
La cadena '0001' es aceptada por el autómata.
La cadena '01' no es aceptada por el autómata.
La cadena '001' no es aceptada por el autómata.
La cadena '00011' no es aceptada por el autómata.
La cadena '11' no es aceptada por el autómata.
```

##

Este proyecto fue desarrollado como parte de un laboratorio de Teoría de la Computación en Universidad del Valle de Guatemala.