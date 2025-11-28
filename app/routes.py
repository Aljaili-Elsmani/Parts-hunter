from flask import render_template, request, redirect, url_for
from app import app
import sqlite3
import os

# مسار قاعدة البيانات
DB_NAME = os.path.join(os.path.dirname(__file__), "..", "database.db")

# الصفحة الرئيسية
@app.route("/")
def index():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

# صفحة إدارة المنتجات
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        category = request.form["category"]

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
                  (name, price, category))
        conn.commit()
        conn.close()
        return redirect(url_for("admin"))

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("admin.html", products=products)

# حذف منتج
@app.route("/delete/<int:id>")
def delete_product(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("admin"))

# صفحة الاتصال بنا
@app.route("/contact")
def contact():
    return render_template("contact.html")

# صفحة حول الموقع
@app.route("/about")
def about():
    return render_template("about.html")
