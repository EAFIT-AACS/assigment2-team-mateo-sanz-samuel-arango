def simulate_pda(string):
    
    stack = ['S']  
    steps = []  
    state = 'q'  

    steps.append((state, string, ''.join(stack)))  # Inic st

    while stack:
        top = stack.pop()  

        if top == 'S':
            if string and string[0] == 'a' and string[-1] == 'b':
                if len(string) > 2:  
                    stack.append('B')  
                    stack.append('S')  
                else:
                    stack.append('B')  
                string = string[1:-1]  

        elif top == 'B':
            pass  # `B` solo sirve como marcador, no cambia la cadena

        # Guardamos el estado actual del PDA
        steps.append((state, string, ''.join(stack) if stack else 'ε'))  

    # Imprimir el proceso paso a paso en consola
    print("Simulación del PDA en la cadena de entrada:")
    for step in steps:
        print(step)


if __name__ == "__main__":
    try:
        with open("accepted_strings.txt", "r") as file:
            strings = [line.strip() for line in file.readlines()]

        for s in strings:
            simulate_pda(s)  # Simular el PDA con cada cadena aceptada

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'accepted_strings.txt'.")
