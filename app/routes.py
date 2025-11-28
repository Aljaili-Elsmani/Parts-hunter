from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "database.db"

# إنشاء قاعدة البيانات إذا لم تكن موجودة
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price TEXT NOT NULL,
                        category TEXT NOT NULL,
                        whatsapp_msg TEXT
                    )''')
        conn.commit()
        conn.close()

init_db()

@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        category = request.form["category"]
        whatsapp_msg = "هل المنتج متوفر؟"  # رسالة واتساب موحدة
        c.execute("INSERT INTO products (name, price, category, whatsapp_msg) VALUES (?, ?, ?, ?)",
                  (name, price, category, whatsapp_msg))
        conn.commit()
        return redirect(url_for("admin"))

    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("admin.html", products=products)

@app.route("/delete/<int:product_id>")
def delete(product_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run(debug=True, port=10000)
