from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # ضروري للسماح للفرونت إند بالوصول للبيانات

products = {
    "1": {"name": "Toyota Camry", "details": "2.5L Engine, Hybrid, 2024 model"},
    "2": {"name": "Honda Accord", "details": "1.5L Turbo, Sedan, 2024 model"},
    "3": {"name": "Ford Explorer", "details": "3.5L V6, SUV, 2024 model"}
}

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
