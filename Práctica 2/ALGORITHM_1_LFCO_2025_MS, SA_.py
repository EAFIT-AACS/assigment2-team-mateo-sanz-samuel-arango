import random

def genera_string_valido():
    """Generamos un string válido basado en la gramática S -> aSb | ε con profundidad aleatoria."""
    depth = random.randint(1, 5)  # Genera un valor aleatorio para la profundidad entre 1 y 5
    return genera_string_valido_con_depth(depth)

def genera_string_valido_con_depth(depth):
    """Función auxiliar que genera el string válido usando recursión."""
    if depth == 0:
        return ""
    return "a" + genera_string_valido_con_depth(depth - 1) + "b"

def genera_string_invalido():
    """Generamos un string inválido con el mismo alfabeto pero que no pertenece al lenguaje."""
    length = random.randint(2, 6)
    return "".join(random.choice("ab") for _ in range(length))

def generar_y_guardar_strings():
    """Genera cadenas válidas e inválidas, las guarda en un archivo y las imprime en consola."""
    valid_strings = [genera_string_valido() for _ in range(3)]  # Genera 3 cadenas válidas con depth aleatorio
    invalid_strings = [genera_string_invalido() for _ in range(2)]  # Genera 2 cadenas inválidas

    all_strings = valid_strings + invalid_strings
    random.shuffle(all_strings)

    with open("generated_strings.txt", "w") as file:
        for s in all_strings:
            file.write(s + "\n")
            print(f"String generado: '{s}'")  # Imprimir en consola

    print("Cadenas generadas y guardadas en el archivo 'generated_strings.txt'.")

if __name__ == "__main__":
    generar_y_guardar_strings()
