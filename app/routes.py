from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قائمة المنتجات (يمكن تعديلها أو الحذف والإضافة مباشرة)
products = [
    {"id": 1, "category": "سيارات", "name": "كمبروسر تويوتا", "price": "3000 جنيه", "whatsapp_message": "مرحباً، أريد الاستفسار عن كمبروسر تويوتا."},
    {"id": 2, "category": "أدوات كهربائية", "name": "مثقاب كهربائي", "price": "1500 جنيه", "whatsapp_message": "مرحباً، أحتاج معلومات عن المثقاب الكهربائي."},
    {"id": 3, "category": "معدات تعدين", "name": "معدات تعدين صغيرة", "price": "5000 جنيه", "whatsapp_message": "مرحباً، أريد تفاصيل عن معدات التعدين."},
    {"id": 4, "category": "معدات طاقة شمسية", "name": "لوحة شمسية 200 واط", "price": "7000 جنيه", "whatsapp_message": "مرحباً، أحتاج معلومات عن اللوحة الشمسية 200 واط."}
]

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html", products=products)

# إضافة منتج
@app.route("/add_product", methods=["POST"])
def add_product():
    global products
    name = request.form.get("name")
    category = request.form.get("category")
    price = request.form.get("price")
    whatsapp_message = request.form.get("whatsapp_message")
    
    if name and category and price:
        new_id = max([p['id'] for p in products], default=0) + 1
        products.append({
            "id": new_id,
            "name": name,
            "category": category,
            "price": price,
            "whatsapp_message": whatsapp_message or f"مرحباً، أريد الاستفسار عن {name}."
        })
    return redirect(url_for('home'))

# حذف منتج
@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
