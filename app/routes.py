from flask import render_template
from app import app

# المنتجات مقسمة حسب الفئة
products = {
    "سيارات": [
        {
            "id": 1,
            "name": "محرك نيسان مستعمل",
            "image": "/static/uploads/engine.jpg",
            "price": "12000 جنيه",
            "whatsapp_message": "مرحباً، أحتاج معلومات عن محرك نيسان المستعمل."
        },
        {
            "id": 2,
            "name": "كمبروسر تويوتا",
            "image": "/static/uploads/compressor.jpg",
            "price": "3000 جنيه",
            "whatsapp_message": "مرحباً، أريد الاستفسار عن كمبروسر تويوتا."
        }
    ],
    "أدوات كهربائية": [
        {
            "id": 3,
            "name": "مثقاب كهربائي",
            "image": "/static/uploads/drill.jpg",
            "price": "1500 جنيه",
            "whatsapp_message": "أريد شراء المثقاب الكهربائي."
        }
    ],
    "معدات تعدين": [
        {
            "id": 4,
            "name": "جهاز كشف ذهب",
            "image": "/static/uploads/gold_detector.jpg",
            "price": "25000 جنيه",
            "whatsapp_message": "أريد معرفة المزيد عن جهاز كشف الذهب."
        }
    ],
    "معدات طاقة شمسية": [
        {
            "id": 5,
            "name": "لوحة شمسية 100 واط",
            "image": "/static/uploads/solar_panel.jpg",
            "price": "5000 جنيه",
            "whatsapp_message": "أريد شراء لوحة شمسية 100 واط."
        }
    ]
}

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/order")
def order():
    return "صفحة الطلب ستضاف لاحقاً"

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")
