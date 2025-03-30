import numpy as np
from scipy.integrate import quad
from sympy import sympify, symbols

function_input = input("Enter a simple mathematical function (use 'x' as the variable): ")

lo = float(input("Enter the lower limit of integration: "))
hi = float(input("Enter the upper limit of integration: "))

# Use sympy to parse the function
function_input = function_input.replace('e', 'exp(1)')  # Replace 'e' with sympy's exp(1)
parsed_function = sympify(function_input)

x = symbols('x')  # Define the symbol for use in the lambda function
fun = quad(lambda x_val: parsed_function.evalf(subs={x: x_val}), lo, hi)

print(f"The result of the integration is: {fun[0]}")