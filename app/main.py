#addition function
def addition(a,b):
        c = a + b
        return c
# Subraction funtion
def subtraction(x, y):
    s = x - y
    return s
# Multiplication funtion
def multiplication(w, e):
    q = w * e
    return q
# division funtion
def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero please provide valid number.")  # Fix the typo
    return a / b
