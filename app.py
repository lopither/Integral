from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scipy.integrate import quad
from sympy import sympify, symbols, lambdify
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Make sure 'index.html' is inside the 'templates/' folder

@app.route('/integrate', methods=['POST'])
def integrate():
    try:
        data = request.json
        function_input = data['function']
        lo = float(data['lower_limit'])
        hi = float(data['upper_limit'])

        # Replace 'e' with sympy's exp(1)
        function_input = function_input.replace('e', 'exp(1)')
        x = symbols('x')
        parsed_function = sympify(function_input)

        # Convert sympy function into a Python function
        func = lambdify(x, parsed_function, modules=['numpy'])

        # Perform numerical integration
        result, _ = quad(func, lo, hi)
        
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
