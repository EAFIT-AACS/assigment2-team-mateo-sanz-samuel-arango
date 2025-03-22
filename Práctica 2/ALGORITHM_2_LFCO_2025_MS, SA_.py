def pda_accepts(string):
    """Simula un PDA que acepta cadenas de la forma a^n b^n."""
    stack = []
    
    for char in string:
        if char == 'a':
            stack.append('a')  # Apilar a
        elif char == 'b':
            if not stack:
                return False  # si no hay a en la pila, es inválido
            stack.pop()  # Desapilar a
        else:
            return False  # caracter inválido

    return len(stack) == 0  # pila vacía


def process_strings():
    """Lee las cadenas generadas, las evalúa con el PDA y guarda las aceptadas."""
    try:
        with open("generated_strings.txt", "r") as file:
            strings = [line.strip() for line in file.readlines()]  # Leer cadenas del archivo
        
        accepted_strings = []
        for s in strings:
            if pda_accepts(s):
                accepted_strings.append(s)
            result = "aceptado ✅" if pda_accepts(s) else "rechazado ❌"
            print(f"El string '{s}' es {result} por el PDA.")
        
        # Guardar las cadenas aceptadas en un archivo
        with open("accepted_strings.txt", "w") as file:
            for s in accepted_strings:
                file.write(s + "\n")
        
        print("Cadenas aceptadas guardadas en 'accepted_strings.txt'.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'generated_strings.txt'.")


if __name__ == "__main__":
    process_strings()
