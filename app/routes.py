from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_PATH = "database.db"

# الصفحة الرئيسية
@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

# صفحة إدارة المنتجات
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        whatsapp_message = request.form.get('whatsapp_message', "هل المنتج متوفر؟")

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO products (name, price, category, whatsapp_message) VALUES (?, ?, ?, ?)",
                  (name, price, category, whatsapp_message))
        conn.commit()
        conn.close()
        return redirect(url_for('admin'))

    # عرض جميع المنتجات
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("admin.html", products=products)

# حذف المنتج
@app.route('/delete/<int:id>')
def delete_product(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True)
