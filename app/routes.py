from flask import render_template, request, redirect, url_for, flash
from app import app
import sqlite3
import os

DB_PATH = "app/database.db"

# إنشاء قاعدة البيانات إذا لم تكن موجودة
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                category TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

init_db()

# الصفحة الرئيسية
@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

# صفحة الإدارة لإضافة وحذف المنتجات
@app.route("/admin", methods=["GET", "POST"])
def admin():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        category = request.form.get("category")

        if name and price and category:
            c.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)", 
                      (name, price, category))
            conn.commit()
            flash("تمت إضافة المنتج بنجاح!", "success")
        return redirect(url_for("admin"))

    # جلب جميع المنتجات لعرضها في صفحة الإدارة
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("admin.html", products=products)

# حذف منتج
@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    flash("تم حذف المنتج بنجاح!", "success")
    return redirect(url_for("admin"))

# صفحة الاتصال بنا
@app.route("/contact")
def contact():
    return render_template("contact.html")

# صفحة حول الموقع
@app.route("/about")
def about():
    return render_template("about.html")
