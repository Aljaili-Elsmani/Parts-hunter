from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قائمة المنتجات فارغة في البداية
products = []

# الصفحة الرئيسية (عرض المنتجات فقط)
@app.route("/")
def home():
    return render_template("index.html", products=products)

# صفحة الإدارة لإضافة وحذف المنتجات
@app.route("/admin", methods=["GET", "POST"])
def admin():
    global products
    if request.method == "POST":
        # إضافة منتج جديد
        name = request.form.get("name")
        price = request.form.get("price")
        category = request.form.get("category")
        if name and price and category:
            product_id = len(products) + 1
            products.append({
                "id": product_id,
                "name": name,
                "price": price,
                "category": category
            })
        return redirect(url_for("admin"))
    return render_template("admin.html", products=products)

# حذف منتج
@app.route("/delete/<int:id>")
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return redirect(url_for("admin"))

# تشغيل التطبيق
if __name__ == "__main__":
    app.run(debug=True)
