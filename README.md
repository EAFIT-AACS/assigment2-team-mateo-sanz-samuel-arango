Aquí tienes el README.md actualizado con los nombres de los autores y el nombre de la práctica:  

---

# **Práctica 2: Context-Free Grammar Processing with PDA and Parse Trees**  

## **Authors**  
- **Mateo Sanz**  
- **Samuel Arango**  

## **System and Tools Used**  
- **Operating System:** Windows 10/11  
- **Programming Language:** Python 3.11  
- **Tools and Libraries:** No external libraries were used  

## **Project Overview**  
This project implements a **Context-Free Grammar (CFG) processor** that generates, validates, and visualizes derivations for strings following the grammar:  

$$ S \to aSb \mid \varepsilon $$  

The system consists of three main algorithms:  
1. **String Generator:** Creates valid and invalid strings based on the grammar.  
2. **Pushdown Automaton (PDA):** Verifies if the generated strings belong to the language.  
3. **Parse Tree Constructor:** Builds a parse tree for each accepted string.  

## **How to Run the Project**  

### **1. Generate Strings**  
Run **Algorithm 1** to create valid and invalid strings:  
```sh
python ALGORITHM_1_LFCO_2025_MS_SA.py
```
This will generate a file **`generated_strings.txt`** containing the strings.  

### **2. Validate Strings with PDA**  
Run **Algorithm 2** to process the generated strings:  
```sh
python ALGORITHM_2_LFCO_2025_MS_SA.py
```
This will output whether each string is **accepted or rejected** and save accepted strings in **`accepted_strings.txt`**.  

### **3. Build and Display Parse Trees**  
Run **Algorithm 3** to construct and display parse trees for the accepted strings:  
```sh
python ALGORITHM_3_LFCO_2025_MS_SA.py
```
This will read **`accepted_strings.txt`**, construct parse trees, and print them hierarchically.  

## **Notes**  
- Ensure that **Python 3.11** is installed and available in the system path.  
- The scripts should be run in the same directory to ensure file dependencies work correctly.  
- The project follows a **structured and modular approach**, making it easy to extend or modify.  

## **Creativity and Enhancements**  
- The PDA simulation includes **emoji-based output** (✅ / ❌) to visually indicate acceptance or rejection.  
- The parse tree uses **indentation-based formatting** to clearly represent hierarchical structure.  
- The approach maintains **clean and readable code**, following best practices in algorithm implementation.  

---
