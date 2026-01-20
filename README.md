# Matrix Operations Tool (Python + NumPy)

## Description
This project is a **menu-driven Matrix Operations Tool** developed using **Python** and **NumPy**.  
It allows users to perform matrix operations interactively while enforcing proper mathematical rules and strong input validation.

The program supports **any matrix size** and prevents invalid operations by checking matrix dimensions before computation.

---

## Features
- Menu-driven user interface
- User selects the operation first
- Supports **any matrix size** (1×3, 2×2, 2×3, 3×3, etc.)
- User can choose:
  - Two matrices (A, B)
  - Three matrices (A, B, C)
- Input validation:
  - Correct number of elements per row
  - Dimension compatibility checks
- Clear error messages for invalid operations
- Uses NumPy for efficient calculations

---

## Supported Operations

### Addition
- Possible only when all matrices have the **same dimensions**
- Supports:
  - A + B
  - A + B + C

### Subtraction
- Possible only when all matrices have the **same dimensions**
- Supports:
  - A − B
  - A − B − C

### Multiplication
- Follows the rule:
A (r₁ × c₁) × B (r₂ × c₂)
c₁ must equal r₂

- Supports:
- A × B
- A × B × C (with validation)

### Transpose
- Works for **any matrix size**
- Converts rows into columns

### Determinant
- Possible **only for square matrices**
- 2×2, 3×3, etc.

---

## Invalid Cases (Handled Safely)
- Addition or subtraction of matrices with different sizes
- Multiplication when column–row rule is violated
- Determinant of non-square matrices
- Incorrect number of values entered per row

The program does **not crash** and instead shows a clear error message.

---

## Technologies Used
- Python 3
- NumPy

---

## How to Run
1. Install NumPy:
 ```bash
 pip install numpy
