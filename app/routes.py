from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# بيانات المنتجات
products = []

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template("index.html", products=products)

# صفحة إدارة المنتجات
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        product = {
            'name': name,
            'price': price,
            'category': category
        }
        products.append(product)
        return redirect(url_for('admin'))
    return render_template("admin.html", products=products)

# حذف منتج
@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(products):
        products.pop(index)
    return redirect(url_for('admin'))

# صفحة اتصل بنا
@app.route('/contact')
def contact():
    return render_template("contact.html")

# صفحة حول الموقع
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000)
