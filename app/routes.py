from flask import render_template, request
from app import app

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/order', methods=["GET", "POST"])
def order():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        item = request.form['item']
        category = request.form['category']
        details = request.form['details']
        print(f"طلب جديد من {name} - {phone}: {item} ({category}) - {details}")
        return "تم استلام الطلب، سنتواصل معك قريبًا!"
    return render_template("order.html")
