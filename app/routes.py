from flask import render_template
from app import app

# قائمة المنتجات (مثال — يمكنك التعديل لاحقاً)
products = [
    {
        "id": 1,
        "name": "كمبروسر تويوتا",
        "image": "/static/uploads/compressor.jpg",
        "price": "3000 جنيه",
        "whatsapp_message": "مرحباً، أريد الاستفسار عن كمبروسر تويوتا."
    },
    {
        "id": 2,
        "name": "محرك نيسان مستعمل",
        "image": "/static/uploads/engine.jpg",
        "price": "12000 جنيه",
        "whatsapp_message": "مرحباً، أحتاج معلومات عن محرك نيسان المستعمل."
    }
]


# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html", products=products)


# صفحة الطلب (اختيارية — لو تحتاج رابط /order)
@app.route("/order")
def order():
    return "صفحة الطلب ستضاف لاحقاً"
