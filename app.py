from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo à minha API Flask!"})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']
        result = num1 + num2
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Parâmetros num1 e num2 são necessários"}), 400

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']
        result = num1 - num2
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Parâmetros num1 e num2 são necessários"}), 400

if __name__ == '__main__':
    app.run(debug=True)
