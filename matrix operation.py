import numpy as np

# ---------- Function to input matrix ----------
def input_matrix(name, rows, cols):
    print(f"\nEnter elements of Matrix {name} ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)


print("\n========== MATRIX OPERATIONS TOOL ==========")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")

choice = int(input("\nEnter your choice (1-5): "))

# =========================================================
# ADDITION & SUBTRACTION
# Rule: All matrices must have SAME rows and columns
# =========================================================
if choice in [1, 2]:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    num = int(input("How many matrices do you want (2 or 3): "))
    if num not in [2, 3]:
        print("Invalid number of matrices.")
        exit()

    A = input_matrix("A", rows, cols)
    B = input_matrix("B", rows, cols)

    if num == 3:
        C = input_matrix("C", rows, cols)

    if choice == 1:
        result = A + B if num == 2 else A + B + C
        print("\nResult (Addition):")
    else:
        result = A - B if num == 2 else A - B - C
        print("\nResult (Subtraction):")

    print(result)


# =========================================================
# MULTIPLICATION
# Rule:
# A (r1 × c1) × B (r2 × c2)
# c1 must equal r2
# =========================================================
elif choice == 3:
    r1 = int(input("Enter rows of Matrix A: "))
    c1 = int(input("Enter columns of Matrix A: "))
    r2 = int(input("Enter rows of Matrix B: "))
    c2 = int(input("Enter columns of Matrix B: "))

    if c1 != r2:
        print("\nMultiplication NOT possible.")
        print(f"Matrix A is {r1}x{c1} and Matrix B is {r2}x{c2}")
        print("Columns of A must equal rows of B.")
        exit()

    A = input_matrix("A", r1, c1)
    B = input_matrix("B", r2, c2)

    num = int(input("How many matrices do you want to multiply (2 or 3): "))

    if num == 3:
        r3 = int(input("Enter rows of Matrix C: "))
        c3 = int(input("Enter columns of Matrix C: "))

        if c2 != r3:
            print("\nMultiplication with Matrix C NOT possible.")
            print("Columns of B must equal rows of C.")
            exit()

        C = input_matrix("C", r3, c3)
        result = np.dot(np.dot(A, B), C)
        print("\nResult (A × B × C):")

    else:
        result = np.dot(A, B)
        print("\nResult (A × B):")

    print(result)


# =========================================================
# TRANSPOSE
# Rule: Works for ANY matrix size
# =========================================================
elif choice == 4:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    A = input_matrix("A", rows, cols)

    print("\nTranspose of Matrix A:")
    print(A.T)


# =========================================================
# DETERMINANT
# Rule: Only for SQUARE matrices (rows == cols)
# =========================================================
elif choice == 5:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows != cols:
        print("\nDeterminant NOT possible.")
        print("Matrix must be square (rows = columns).")
        exit()

    A = input_matrix("A", rows, cols)

    print("\nDeterminant of Matrix A:")
    print(np.linalg.det(A))


else:
    print("\nInvalid choice. Please select between 1 and 5.")
