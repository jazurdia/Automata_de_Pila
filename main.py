class Pila:
    def __init__(self):
        self.items = ["Z0"]

    def esta_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def __str__(self):
        return str(self.items)


class AutomataDePila:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}
        self.estado_actual = 'q0'
        self.entrada = ""
        self.pila = Pila()
        self.estado_aceptacion = {'q2'}

    def reset(self):
        self.estado_actual = 'q0'
        self.pila = Pila()

    def procesar_caracter(self, caracter):
        cima_pila = self.pila.peek()
        if self.estado_actual == 'q0':
            if caracter == '0' and (cima_pila == 'Z0' or cima_pila == 'X'):
                self.pila.pop()
                self.pila.push('X')
                self.pila.push('X')
            elif caracter == '1' and cima_pila == 'X':
                self.estado_actual = 'q1'
                self.pila.pop()
            else:
                return False
        elif self.estado_actual == 'q1':
            if caracter == '1' and cima_pila == 'X':
                self.pila.pop()
            elif caracter == '':
                if cima_pila == 'Z0':
                    self.estado_actual = 'q2'
                    return True
            else:
                return False
        return True

    def procesar_entrada(self, entrada):
        self.reset()
        self.entrada = entrada
        for caracter in self.entrada:
            if not self.procesar_caracter(caracter):
                return False
        if self.estado_actual == 'q1':
            return self.procesar_caracter('')  # procesa el carácter vacío final
        return self.estado_actual in self.estado_aceptacion

    def acepta(self, entrada):
        return self.procesar_entrada(entrada)


# Instancia del autómata de pila
aut = AutomataDePila()

# Ejemplos de cadenas
cadenas = ["00", "0001", "01", "001", "00011", "11"]

# Probar el autómata con las cadenas
for cadena in cadenas:
    resultado = aut.acepta(cadena)
    print(f"La cadena '{cadena}' {'es aceptada' if resultado else 'no es aceptada'} por el autómata.")
