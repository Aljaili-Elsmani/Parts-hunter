from flask import render_template, redirect, url_for, request
from app import app

# بيانات المنتجات (يمكنك التعديل لاحقاً)
products = [
    {"id": 1, "category": "سيارات", "name": "كمبروسر تويوتا", "price": "3000 جنيه", "whatsapp_message": "مرحباً، أريد الاستفسار عن كمبروسر تويوتا."},
    {"id": 2, "category": "معدات تعدين", "name": "محرك نيسان مستعمل", "price": "12000 جنيه", "whatsapp_message": "مرحباً، أحتاج معلومات عن محرك نيسان المستعمل."}
]

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html", products=products)

# صفحة الطلب (اختيارية)
@app.route("/order")
def order():
    return "صفحة الطلب ستضاف لاحقاً"

# صفحة اتصل بنا
@app.route("/contact")
def contact():
    return "صفحة اتصل بنا"

# صفحة حول الموقع
@app.route("/about")
def about():
    return "صفحة حول الموقع"

# إضافة منتج جديد (form في المستقبل)
@app.route("/add_product", methods=["POST"])
def add_product():
    name = request.form.get("name")
    category = request.form.get("category")
    price = request.form.get("price")
    message = request.form.get("whatsapp_message")
    if name and category and price:
        new_id = max([p["id"] for p in products]+[0]) + 1
        products.append({
            "id": new_id,
            "category": category,
            "name": name,
            "price": price,
            "whatsapp_message": message
        })
    return redirect(url_for("home"))

# حذف منتج
@app.route("/delete_product/<int:id>")
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return redirect(url_for("home"))
