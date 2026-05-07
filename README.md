# Car Dealership & Microservices Evaluation Project

هذا المشروع هو التطبيق العملي النهائي لنشر الخدمات المصغرة (Microservices) باستخدام تقنيات Cloud Native على منصة IBM Cloud.

## 📁 هيكل المستودع (Repository Structure)

المستودع يحتوي على الملفات التالية:

* `product_details/`
    * `app.py` (خدمة الـ Python)
    * `requirements.txt`
    * `Dockerfile`
* `dealer_pricing/`
    * `server.js` (خدمة الـ Node.js)
    * `package.json`
    * `Dockerfile`
* `frontend/`
    * `index.html` (الواجهة الأمامية المعدلة)
    * `Dockerfile`
* `README.md`

---

## 💻 الأكواد البرمجية (Source Code)

### 1. خدمة تفاصيل المنتج (Python) - `product_details/app.py`
```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # للسماح بالاتصال من الواجهة الأمامية

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
