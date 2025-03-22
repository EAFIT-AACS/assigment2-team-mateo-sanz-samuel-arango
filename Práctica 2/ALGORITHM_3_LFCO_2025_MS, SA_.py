class NodoArbol:
    """Clase para representar un nodo en el árbol de derivación."""
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def imprimir(self, nivel=0):
        """Imprime el árbol con indentación para visualizar la estructura."""
        print("  " * nivel + self.valor)
        for hijo in self.hijos:
            hijo.imprimir(nivel + 1)


def construir_arbol_derivacion(cadena):
    """Construye el árbol de derivación para una cadena generada por la gramática S -> aSb | ε."""
    raiz = NodoArbol("S")
    nodo_actual = raiz
    pila_nodos = []  # Para rastrear el nodo `S` en cada nivel

    for char in cadena:
        if char == "a":
            nuevo_nodo = NodoArbol("aSb")  # Aplicamos S → aSb
            nodo_actual.agregar_hijo(NodoArbol("a"))
            nodo_siguiente = NodoArbol("S")
            nodo_actual.agregar_hijo(nodo_siguiente)
            nodo_actual.agregar_hijo(NodoArbol("b"))
            pila_nodos.append(nodo_actual)  # Guardamos referencia al nodo padre
            nodo_actual = nodo_siguiente  # Avanzamos en la derivación

    nodo_actual.agregar_hijo(NodoArbol("ε"))  # Terminamos la derivación con ε
    return raiz


def leer_cadenas_aceptadas(nombre_archivo):
    """Lee las cadenas aceptadas desde un archivo de texto."""
    try:
        with open(nombre_archivo, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error: No se encontró el archivo de cadenas aceptadas.")
        return []


if __name__ == "__main__":
    archivo_cadenas = "accepted_strings.txt"
    cadenas_aceptadas = leer_cadenas_aceptadas(archivo_cadenas)

    if not cadenas_aceptadas:
        print("No hay cadenas aceptadas para procesar.")
    else:
        for cadena in cadenas_aceptadas:
            print(f"\nÁrbol de derivación para '{cadena}':")
            arbol = construir_arbol_derivacion(cadena)
            arbol.imprimir()
