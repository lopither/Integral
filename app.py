from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scipy.integrate import quad
from sympy import sympify, symbols, lambdify
import numpy as np
import os

app = Flask(__name__)

# Enable CORS for specific origins (Modify "*" to allow only specific domains)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    if not os.path.exists("templates/index.html"):
        return jsonify({'error': "index.html not found in templates folder"}), 500
    return render_template('index.html')

@app.route('/integrate', methods=['POST'])
def integrate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data received'}), 400

        function_input = data.get('function', '').strip()
        if not function_input:
            return jsonify({'error': 'Function is required'}), 400

        lo = data.get('lower_limit')
        hi = data.get('upper_limit')

        if lo is None or hi is None:
            return jsonify({'error': 'Both lower and upper limits are required'}), 400

        lo, hi = float(lo), float(hi)

        # Replace 'e' with sympy's exp(1) for correct parsing
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
    app.run(host='0.0.0.0', port=5000, debug=True)
