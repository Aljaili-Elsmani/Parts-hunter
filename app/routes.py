from flask import render_template, request, redirect, url_for
from app import app
import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "..", "database.db")

# دالة لإنشاء قاعدة البيانات والجدول إذا لم يكن موجودًا
def init_db():
    if not os.path.exists(DB_NAME):
        with sqlite3.connect(DB_NAME) as conn:
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

# الصفحة الرئيسية
@app.route("/")
def index():
    init_db()  # تأكد من وجود الجدول قبل أي استعلام
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

# صفحة إدارة المنتجات
@app.route("/admin", methods=["GET", "POST"])
def admin():
    init_db()
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

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")
