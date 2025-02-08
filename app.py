from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple route to return a greeting
@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

# Route to add two numbers
@app.route('/add/<int:num1>/<int:num2>')
def add_numbers(num1, num2):
    result = num1 + num2
    return jsonify(result=result)

# Route to subtract two numbers
@app.route('/subtract/<int:num1>/<int:num2>')
def subtract_numbers(num1, num2):
    result = num1 - num2
    return jsonify(result=result)

# Route to multiply two numbers
@app.route('/multiply/<int:num1>/<int:num2>')
def multiply_numbers(num1, num2):
    result = num1 * num2
    return jsonify(result=result)

# Route to divide two numbers (handles division by zero)
@app.route('/divide/<int:num1>/<int:num2>')
def divide_numbers(num1, num2):
    if num2 == 0:
        return jsonify(error="Cannot divide by zero"), 400
    result = num1 / num2
    return jsonify(result=result)

# Route to concatenate two strings
@app.route('/concat', methods=['POST'])
def concat_strings():
    data = request.get_json()
    str1 = data.get('str1')
    str2 = data.get('str2')
    if str1 is None or str2 is None:
        return jsonify(error="Both 'str1' and 'str2' are required"), 400
    result = str1 + str2
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
