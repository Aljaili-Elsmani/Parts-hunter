from flask import render_template, request, redirect, url_for
from app import app

# قائمة المنتجات المصنفة
products = {
    "سيارات": [
        {
            "id": 1,
            "name": "كمبروسر تويوتا",
            "image": "/static/uploads/compressor.jpg",
            "price": "3000 جنيه",
            "whatsapp_message": "مرحباً، أريد الاستفسار عن كمبروسر تويوتا."
        }
    ],
    "أدوات كهربائية": [
        {
            "id": 2,
            "name": "مثقاب كهربائي",
            "image": "/static/uploads/drill.jpg",
            "price": "1500 جنيه",
            "whatsapp_message": "مرحباً، أحتاج معلومات عن المثقاب الكهربائي."
        }
    ],
    "معدات تعدين": [],
    "معدات طاقة شمسية": []
}

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html", products=products)

# صفحة إضافة المنتج
@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        category = request.form["category"]
        if category not in products:
            products[category] = []

        new_id = max([p["id"] for plist in products.values() for p in plist], default=0) + 1
        product = {
            "id": new_id,
            "name": request.form["name"],
            "image": request.form["image"],
            "price": request.form["price"],
            "whatsapp_message": request.form["whatsapp_message"]
        }
        products[category].append(product)
        return redirect(url_for("home"))

    return render_template("add_product.html", categories=products.keys())

# حذف المنتج
@app.route("/delete_product/<category>/<int:product_id>")
def delete_product(category, product_id):
    if category in products:
        products[category] = [p for p in products[category] if p["id"] != product_id]
    return redirect(url_for("home"))

# صفحة الطلب
@app.route("/order")
def order():
    return "صفحة الطلب ستضاف لاحقاً"

# صفحة الاتصال
@app.route("/contact")
def contact():
    return render_template("contact.html")

# صفحة حول الموقع
@app.route("/about")
def about():
    return render_template("about.html")
