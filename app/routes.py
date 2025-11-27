from flask import render_template, request, redirect, url_for
from app import app

# المنتجات مخزنة في الذاكرة (يمكن تطويرها لاحقاً لقاعدة بيانات)
products = [
    {"id": 1, "name": "كمبروسر تويوتا", "category": "أدوات كهربائية", "price": "3000 جنيه", "whatsapp": "00249902355371"},
    {"id": 2, "name": "محرك نيسان مستعمل", "category": "سيارات", "price": "12000 جنيه", "whatsapp": "00249902355371"},
]

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html", products=products)

# صفحة الطلب (اختياري)
@app.route("/order")
def order():
    return "صفحة الطلب ستضاف لاحقاً"

# صفحة حول الموقع
@app.route("/about")
def about():
    return render_template("about.html")

# صفحة الاتصال
@app.route("/contact")
def contact():
    return render_template("contact.html")

# إضافة منتج جديد
@app.route("/add_product", methods=["POST"])
def add_product():
    name = request.form.get("name")
    category = request.form.get("category")
    price = request.form.get("price")
    whatsapp = request.form.get("whatsapp") or "00249902355371"
    if name and category and price:
        new_id = max([p["id"] for p in products], default=0) + 1
        products.append({
            "id": new_id,
            "name": name,
            "category": category,
            "price": price,
            "whatsapp": whatsapp
        })
    return redirect(url_for("home"))

# حذف منتج
@app.route("/delete_product/<int:id>", methods=["POST"])
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return redirect(url_for("home"))
