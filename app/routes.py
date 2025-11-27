from flask import render_template, request, redirect, url_for
from app import app

# قائمة المنتجات المبدئية
products = [
    {"id": 1, "name": "كمبروسر تويوتا", "category": "معدات كهربائية", "price": "3000 جنيه", "whatsapp_message": "مرحباً، أريد الاستفسار عن كمبروسر تويوتا."},
    {"id": 2, "name": "محرك نيسان مستعمل", "category": "سيارات", "price": "12000 جنيه", "whatsapp_message": "مرحباً، أحتاج معلومات عن محرك نيسان المستعمل."}
]

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html", products=products)

# صفحة إضافة منتج
@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        new_id = max([p["id"] for p in products], default=0) + 1
        product = {
            "id": new_id,
            "name": request.form["name"],
            "category": request.form["category"],
            "price": request.form["price"],
            "whatsapp_message": request.form["whatsapp_message"]
        }
        products.append(product)
        return redirect(url_for("home"))
    return render_template("add_product.html")

# حذف منتج
@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return redirect(url_for("home"))
