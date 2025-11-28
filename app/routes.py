from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# اسم ملف قاعدة البيانات
DB_FILE = "database.db"

# دالة للتأكد من وجود قاعدة البيانات وإنشائها إذا لم تكن موجودة
def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''CREATE TABLE products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price TEXT NOT NULL,
                        category TEXT NOT NULL
                     )''')
        conn.commit()
        conn.close()

# استدعاء الدالة عند تشغيل التطبيق
init_db()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO products (name, price, category) VALUES (?, ?, ?)", (name, price, category))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("admin.html", products=products)

@app.route('/delete/<int:product_id>')
def delete_product(product_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000)
