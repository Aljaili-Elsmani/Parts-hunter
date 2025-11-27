from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قائمة المنتجات (مثال)
products = [
    {"id": 1, "name": "كمبروسر تويوتا", "price": "3000 جنيه", "category": "سيارات"},
    {"id": 2, "name": "محرك نيسان مستعمل", "price": "12000 جنيه", "category": "معدات تعدين"},
    {"id": 3, "name": "دربكين كهرباء", "price": "2000", "category": "أدوات كهربائية"}
]

# الصفحة الرئيسية
@app.route("/")
def index():
    return render_template("index.html", products=products)

# صفحة إدارة المنتجات
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        # إضافة منتج جديد
        new_id = max([p["id"] for p in products]) + 1 if products else 1
        name = request.form.get("name")
        price = request.form.get("price")
        category = request.form.get("category")
        products.append({"id": new_id, "name": name, "price": price, "category": category})
        return redirect(url_for("admin"))
    return render_template("admin.html", products=products)

# حذف المنتج
@app.route("/delete/<int:id>")
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return redirect(url_for("admin"))

# صفحة اتصل بنا
@app.route("/contact")
def contact():
    return render_template("contact.html")

# صفحة حول الموقع
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
