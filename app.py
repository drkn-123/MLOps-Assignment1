from flask import Flask, request, jsonify

app = Flask(__name__)

# Addition
@app.route('/add', methods=['GET'])
def add():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    return jsonify({"result": num1 + num2})

# Subtraction
@app.route('/subtract', methods=['GET'])
def subtract():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    return jsonify({"result": num1 - num2})

# Multiplication
@app.route('/multiply', methods=['GET'])
def multiply():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    return jsonify({"result": num1 * num2})

# Division
@app.route('/divide', methods=['GET'])
def divide():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 1))  # Default to 1 to avoid division by zero
    if num2 == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    return jsonify({"result": num1 / num2})

if __name__ == '__main__':
    app.run(debug=True)
