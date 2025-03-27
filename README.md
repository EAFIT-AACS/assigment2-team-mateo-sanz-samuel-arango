# PDA Simulation for Context-Free Language Recognition

## Authors
**Mateo Sanz** & **Samuel Arango**

## Description
This project contains three Python algorithms that work together to generate, validate, and simulate a pushdown automaton (PDA) for recognizing strings in the language described by the grammar:

\[ S \to aSb \ | \ \varepsilon \]

The PDA accepts strings of the form `a^n b^n`, ensuring a balanced sequence of 'a' followed by 'b'.

## Files and Their Functionality

### 1. `ALGORITHM_1_LFCO_2025_MS_SA.py` - String Generation
This script generates random valid and invalid strings based on the grammar and saves them to `generated_strings.txt`.

- **Valid Strings:** Generated using recursive calls that insert 'a' at the beginning and 'b' at the end.
- **Invalid Strings:** Randomly created with characters 'a' and 'b' but not necessarily following the grammar.

### 2. `ALGORITHM_2_LFCO_2025_MS_SA.py` - PDA Validation
This script reads the generated strings and processes them using a simulated PDA.

- If the PDA recognizes the string as valid (`a^n b^n` structure), it is saved in `accepted_strings.txt`.
- The script outputs whether each string is **accepted ✅** or **rejected ❌**.

### 3. `ALGORITHM_3_LFCO_2025_MS_SA.py` - PDA Simulation Steps
This script simulates the step-by-step execution of the PDA for each accepted string.

- It maintains a stack and processes each character based on PDA rules.
- The transitions are displayed to show how the PDA processes input strings.

## How to Run the Project
Ensure you have Python installed, then execute the scripts in the following order:

1. **Generate Strings:**
   ```bash
   python ALGORITHM_1_LFCO_2025_MS_SA.py
   ```
2. **Validate with PDA:**
   ```bash
   python ALGORITHM_2_LFCO_2025_MS_SA.py
   ```
3. **Simulate PDA Execution:**
   ```bash
   python ALGORITHM_3_LFCO_2025_MS_SA.py
   ```

## Output Files
- `generated_strings.txt` → Contains valid and invalid generated strings.
- `accepted_strings.txt` → Stores only valid strings recognized by the PDA.

## Notes
- Ensure that `generated_strings.txt` exists before running the PDA validation script.
- If `accepted_strings.txt` is empty, it means no valid strings were found.



